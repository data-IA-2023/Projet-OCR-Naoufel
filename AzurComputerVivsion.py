import os
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
            # Print caption results to the console
            print(" Caption:")
            #if result.caption is not None:
                
                #print(f"   '{result.caption.text}', Confidence {result.caption.confidence:.4f}")

            # Print text (OCR) analysis results to the console
            print(" Read:")
            if result.read is not None:
                for line in result.read.blocks[0].lines:
                    print(f"   Ligne: '{line.text}', Position {line.bounding_polygon}")
                    liste.append(line.text)
                    #for word in line.words:
                        #print(f"     mots: '{word.text}', Position {word.bounding_polygon}, Confiance {word.confidence:.4f}")
            dico_ocr[titre]=liste      
    return












