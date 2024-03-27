

from dotenv import load_dotenv
import pytesseract
from PIL import Image, ImageEnhance
import requests
from io import BytesIO
import os





def OCR(doc, url):
    load_dotenv()

    try:
        endpoint = os.environ["VISION_ENDPOINT"]
        key = os.environ["VISION_KEY"]
    except KeyError:
        print("Missing environment variable 'VISION_ENDPOINT' or 'VISION_KEY'")
        print("Set them before running this sample.")
        exit()

    resultats = []
    
    for cle in doc.keys():
        for titre in doc[cle]:
            # Téléchargement de l'image depuis l'URL
            response = requests.get(url + f"/{titre}")
            status = response.status_code
    
            # Vérification du statut de la réponse
            if status == 200:
                # Ouvrir l'image depuis le contenu de la réponse
                image = Image.open(BytesIO(response.content))

                # Conversion de l'image en niveaux de gris
                image = image.convert("L")

                # Augmentation du contraste de l'image
                enhancer = ImageEnhance.Contrast(image)
                image = enhancer.enhance(10)  # Augmentation du contraste (ajuster selon vos besoins)

                # Binarisation de l'image
                image = image.point(lambda x: 0 if x < 128 else 255, '1')

                # Conversion de l'image en texte
                texte = pytesseract.image_to_string(image, lang='fra')
                
                # Ajouter les résultats à la liste
                resultats.append({"titre": titre, "texte": texte, "status": status})
                print("------------------")
                # Affichage du texte extrait
                print(f"Titre: {titre}")
                print(texte)
                print("\n")  # Ajouter une ligne vide pour la lisibilité

  
                
              
          


      







"""
def OCR(dico,url):
   
print(OCR("https://invoiceocrp3.azurewebsites.net/invoices/FAC_2019_1001-1741067"))



def OCR(doc,url):
    dico_ocr = {}
    
    load_dotenv()
    for key in doc.keys():
        #yolo = doc[key]
        for titre in doc[key]:
            liste = []
            try:
                endpoint = os.environ["VISION_ENDPOINT"]
                key = os.environ["VISION_KEY"]
            except KeyError:
                print("Missing environment variable 'VISION_ENDPOINT' or 'VISION_KEY'")
                print("Set them before running this sample.")
                exit()
            # Create an Image Analysis client
            client = ImageAnalysisClient(
                endpoint=endpoint,
                credential=AzureKeyCredential(key)
            )
            #for mon_fichier in liste:
            # Get a caption for the image. This will be a synchronously (blocking) call.
            result = client.analyze_from_url(
                image_url= url+ f"/{titre}",
                visual_features=[VisualFeatures.CAPTION, VisualFeatures.READ],
                gender_neutral_caption=True,  # Optional (default is False)
            )

            print("-----------Resultat Analyse OCR---------------:")
            print(titre)
            print(" Read:")
            if result.read is not None:
                for line in result.read.blocks[0].lines:
                    print(line.text, line.bounding_polygon)
                    liste.append(line.text)
                    dico_ocr[titre]=liste
                
                    #for word in line.words:
                        #print(f"     mots: '{word.text}', Position {word.bounding_polygon}, Confiance {word.confidence:.4f}")

           
            
      

    return dico_ocr
"""