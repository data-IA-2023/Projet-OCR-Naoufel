from PIL import Image, ImageEnhance,ImageFilter
from io import BytesIO
import os


def telecharger_modif_img(response):
    """
    Fonction qui effectue du préprocessing sur les images avant de les envoyées à l'OCR
    INPUT: response(larequete vers l'API contenant les factures)
    OUTPUT: None(L'image est stockées en Locale)
    """
    # Ouvrir l'image depuis le contenu de la réponse
    image = Image.open(BytesIO(response.content))
    # Conversion de l'image en niveaux de gris
    image = image.convert("L")
    # Augmentation du contraste de l'image
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(20)  # Augmentation du contraste (ajuster selon vos besoins)
    image = image.filter(ImageFilter.SHARPEN)
    # Binarisation de l'image
    image = image.point(lambda x: 0 if x < 128 else 255, '1')
    # Définir le chemin local où vous souhaitez enregistrer l'image
    nom_fichier = "stockage.jpg"  # Nom de fichier de votre choix avec l'extension correspondante
    # Chemin complet vers le fichier local
    chemin_local = os.path.join("C:/Users/naouf/Documents/1-Naoufel/1-projet/6-OCR/Projet-OCR-Naoufel", nom_fichier)  
    # Enregistrer l'image localement
    with open(chemin_local, "wb") as f:
        f.write(response.content)
    return 




 

