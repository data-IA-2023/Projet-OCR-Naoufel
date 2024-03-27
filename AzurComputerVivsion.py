"""import os
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv
# Set the values of your computer vision endpoint and computer vision key
# as environment variables:

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
                    print(line.text,)
                    liste.append(line.text)
                    dico_ocr[titre]=liste
                
                    #for word in line.words:
                        #print(f"     mots: '{word.text}', Position {word.bounding_polygon}, Confiance {word.confidence:.4f}")
            
      

    return dico_ocr"""



from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from msrest.authentication import CognitiveServicesCredentials
import os
from dotenv import load_dotenv
import time

load_dotenv()

dico = {}

# Authenticate
subscription_key = os.environ["VISION_KEY"]
endpoint = os.environ["VISION_ENDPOINT"]

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

print("===== Read File =====")
read_image_url = "https://invoiceocrp3.azurewebsites.net/invoices/FAC_2024_0009-8145984"

# Call API with URL and raw response
read_response = computervision_client.read(read_image_url,  raw=True)

read_operation_location = read_response.headers["Operation-Location"]
operation_id = read_operation_location.split("/")[-1]

while True:
    read_result = computervision_client.get_read_result(operation_id)
    if read_result.status not in ['notStarted', 'running']:
        break
    time.sleep(1)

if read_result.status == OperationStatusCodes.succeeded:
    for text_result in read_result.analyze_result.read_results:
        for line in text_result.lines:
            dico[line.text] = line.bounding_box

print("End of Computer Vision ")

# Fonction pour vérifier si deux boîtes englobantes sont sur la même ligne horizontale
def same_horizontal_line(box1, box2):
    # Compare les coordonnées y des deux boîtes englobantes avec une tolérance de 5 pixels
    return abs(box1[1] - box2[1]) < 5  # Tolérance de 5 pixels


# Groupe les mots sur la même ligne
grouped_lines = {}

# Parcoure le dictionnaire
for text, bbox in dico.items():
    # Vérifie si la ligne existe déjà dans grouped_lines
    if len(grouped_lines) == 0:
        grouped_lines[0] = []
        grouped_lines[0].append(text)
    else:
        # Vérifie si le texte est sur la même ligne qu'un texte précédent
        grouped = False
        for group_key, group_value in grouped_lines.items():
            group_bbox = dico[group_value[0]]
            if same_horizontal_line(bbox, group_bbox):
                grouped_lines[group_key].append(text)
                grouped = True
                break
        # Si le texte n'est pas sur la même ligne qu'un texte précédent, crée une nouvelle ligne
        if not grouped:
            new_key = max(grouped_lines.keys()) + 1
            grouped_lines[new_key] = [text]

# Affiche les lignes groupées
for key, value in grouped_lines.items():
    print("Texte extrait de la ligne", key + 1, ":")
    print(" ".join(value))
    print("=" * 30)