from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials


import os
import time

import time

def OCR(titre):
    print(titre)
    liste = []
    '''
    Authenticate
    Authenticates your credentials and creates a client.
    '''
    url = os.environ["URL"]
    subscription_key = os.environ["VISION_KEY"]
    endpoint = os.environ["VISION_ENDPOINT"]
    computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))
    image_url =f"{url}/{titre}"
    print("===== Tag an image - remote =====")
    read_response = computervision_client.read(image_url,  raw=True)# Call API with URL and raw response (allows you to get the operation location)# Call API with remote image
    read_operation_location = read_response.headers["Operation-Location"]
    operation_id = read_operation_location.split("/")[-1]
    while True:
        read_result = computervision_client.get_read_result(operation_id)
        if read_result.status not in ['notStarted', 'running']:
            break
        time.sleep(1)
    if read_result.status == OperationStatusCodes.succeeded:
        for text_result in read_result.analyze_result.read_results:
            
            preligne = ""
            preH = 150
            
            for line in text_result.lines:
                if abs(line.bounding_box[-1]-preH)<9:

                    if preH == None:
                        preH = line.bounding_box[-1]
                    
                    preligne = preligne + f' {line.text}'
                    if liste[-1] in preligne:
                        liste[-1]= preligne
                    print("preH",preH)
                    print("preligne",preligne)
                    print('-----------------------')
                else:
                    preH = line.bounding_box[-1]
                    preligne = line.text
                    print("line.text",line.text)
                    print("line.box",line.bounding_box[-1])
                    print("preligne",preligne)
                    print(preH)
                    liste.append(line.text)
            
                    
                print("------------------------------------------LIGNE SUIVANTE--------------------------------")
            print(liste)

               
    print()
    print("End of Computer Vision quickstart.")

    return







""" # Récupérer les coordonnées y de la boîte de délimitation de la ligne
                y_coordinate = line.bounding_box[1]

                # Si la coordonnée y existe déjà dans le dictionnaire, ajouter la ligne à la liste correspondante
                if y_coordinate in lines_by_y:
                    lines_by_y[y_coordinate].append(line)
                # Sinon, créer une nouvelle liste avec la ligne
                else:
                    lines_by_y[y_coordinate] = [line]

        # Trier les lignes par coordonnée y
        sorted_lines = sorted(lines_by_y.items(), key=lambda x: x[0])

        # Parcourir les groupes de lignes
        for _, lines in sorted_lines:
            # Trier les lignes par coordonnée x
            sorted_lines_x = sorted(lines, key=lambda x: x.bounding_box[0])

            # Récupérer les textes des lignes
            texts = [line.text.strip() for line in sorted_lines_x]

            # Fusionner les textes proches horizontalement
            merged_texts = []
            current_text = texts[0]
            for text in texts[1:]:
                # Récupérer les coordonnées x maximales de la ligne actuelle et précédente
                x_max_current = sorted_lines_x[texts.index(text)].bounding_box[2]
                x_max_prev = sorted_lines_x[texts.index(current_text)].bounding_box[2]
                # Si la distance horizontale entre les lignes est inférieure à 50, fusionner les textes
                if x_max_current - x_max_prev < 10:
                    current_text += ' ' + text
                else:
                    merged_texts.append(current_text)
                    current_text = text
            merged_texts.append(current_text)

            # Afficher les lignes fusionnées
            for text in merged_texts:
                print(text)
            print()"""










"""def OCR(titre):
    '''
    Authenticate
    Authenticates your credentials and creates a client.
    '''
    url = os.environ["URL"]
    subscription_key = os.environ["VISION_KEY"]
    endpoint = os.environ["VISION_ENDPOINT"]
    computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))
    image_url =f"{url}/{titre}"
    print("===== Tag an image - remote =====")
    read_response = computervision_client.read(image_url,  raw=True)# Call API with URL and raw response (allows you to get the operation location)# Call API with remote image
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
                print(line.text)
                #print(line.bounding_box)
    print()
    print("End of Computer Vision quickstart.")

    return"""