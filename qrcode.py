import requests

# Fonction pour décoder un QR code à partir d'une image en utilisant une API en ligne
def decode_qr_code():
    """
    Fonction qui effectue une requete vers une api afin d'y récupérer les données stockées dans le qrcode 
    Il en ressort un dictionnaire comprenant les données et le status de la requete
    INPUT: None
    OUTPUT: dicti
    """
    # URL de l'API de décodage des QR codes
    image_path = "stockage.jpg"
    api_url = "https://api.qrserver.com/v1/read-qr-code/"
    # Chargement de l'image
    with open(image_path, 'rb') as file:
        files = {'file': file}
        response = requests.post(api_url, files=files)
        status = response.status_code
    # Analyse de la réponse JSON
    if status == 200:
        data = response.json()
        dicti = {}
        if data and 'symbol' in data[0]:
            for element in data[0]['symbol'][0]['data'].split("\n"):
                dicti[element.split(":")[0]] = element.split(":")[1]
            dicti["status_request"]=status
            return dicti
            #return data[0]['symbol'][0]['data']
        else:
            return "Aucun QR code détecté dans l'image."
    else:
        return "Erreur lors de la requête à l'API."
# Chemin de l'image contenant le QR code





