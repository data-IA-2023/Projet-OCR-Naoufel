import requests
from bs4 import BeautifulSoup

# URL du site à scraper
url = 'https://www.tours.fr/'

# Effectuer une requête GET vers le site
response = requests.get(url)

# Vérifier si la requête a réussi
if response.status_code == 200:
    # Analyser le contenu HTML avec Beautiful Soup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Trouver tous les éléments ayant la classe "new item"
    new_items = soup.find_all(class_='news-item')

    # Parcourir chaque élément "new item" et extraire les titres, les images et les liens
    for item in new_items:
        # Récupérer le titre s'il existe
        title = item.find('p')
        title_text = title.text.strip() if title else 'Aucun titre trouvé'

        # Récupérer l'image s'il existe
        image = item.find('img')
        image_source = image.get('data-src') if image else 'Aucune image trouvée'

        # Récupérer le lien s'il existe
        link = item.find('a')
        link_href = link['href'] if link else 'Aucun lien trouvé'

        # Afficher les résultats
        print("Titre:", title_text)
        print("Image:", image_source)
        print("Lien:", link_href)
        print("\n")

else:
    print('La requête a échoué avec le code :', response.status_code)