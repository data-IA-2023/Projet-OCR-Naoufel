from dotenv import load_dotenv
import requests
import os

load_dotenv()

def rechercheNom(année):
    liste = []
    url = os.getenv('URL')
    header = {'Accept': 'application/json'}
    response = requests.get(url+f"?start_date={année}-01", headers = header)
    status = response.status_code 
    #print(response)   
        # Vérifier si la requête a réussi (code de statut 200)
    if response.content:
        # Afficher le contenu de la réponse (les documents)
        documents = response.json()
        for doc in documents["invoices"]:
            #print(doc)
            liste.append(doc['no'])
    else:
        # Si la requête a échoué, afficher le code d'erreur
        print(f"La requête a échoué avec le code d'erreur : {response.status_code}")
    return liste , status , url




def année(année):
    dico = {}
    while True:
        
        try:
            liste , status , url = rechercheNom(année)
            if liste == [] or liste == None:
                break
            else:
                dico[année] = liste
                année+=1
            
        except:
            print("Error documents non trouvés")
            break
    return liste , status , url , dico



"""
def telecharger_images(liste,url):
    dossier_destination  = "C:/Users/naouf/Documents/1-Naoufel/1-projet/6-OCR/Projet-OCR-Naoufel/ImagesFactures"
    for nom_image in liste:
        # Créer le dossier de destination s'il n'existe pas
        if not os.path.exists(dossier_destination):
            os.makedirs(dossier_destination)

        # Lien à partir duquel vous souhaitez récupérer l'image
        lien_image = url+f"/{nom_image}"
        # Envoyer une requête GET pour récupérer le contenu du lien
        reponse = requests.get(lien_image)
        
        # Vérifier si la requête a réussi
        if reponse.status_code == 200:
            # Parcourir le contenu de la réponse
            contenu = reponse.content
            # Nommer le fichier
            nom_fichier = f"{nom_image}.png"
            # Chemin complet du fichier de destination
            
            chemin_destination = os.path.join(dossier_destination, nom_fichier)
            # Écrire le contenu de l'image dans un fichier
            with open(chemin_destination, "wb") as fichier:
                fichier.write(contenu)
            print("Téléchargement réussi :", nom_fichier)
        else:
            print("Échec du téléchargement :", reponse.status_code)
    return

"""