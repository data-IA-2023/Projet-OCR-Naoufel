import cv2
import pytesseract

# Charger l'image
image = cv2.imread('ImagesFactures/FAC_2019_0996-2430974.png')

# Convertir l'image en niveaux de gris
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Appliquer une binarisation (si nécessaire)
_, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Trouver les contours dans l'image
contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Créer une copie de l'image originale pour dessiner les contours
contour_img = image.copy()

# Liste pour stocker les régions segmentées
segmented_regions = []

# Parcourir les contours
for contour in contours:
    # Obtenez les coordonnées du rectangle englobant pour chaque contour
    x, y, w, h = cv2.boundingRect(contour)
    
    # Dessinez le rectangle sur l'image contour_img (optionnel, pour visualisation)
    cv2.rectangle(contour_img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    # Extraire chaque région de l'image originale en utilisant les coordonnées du rectangle
    region = image[y:y+h, x:x+w]
    
    # Ajouter la région extraite à la liste des régions segmentées
    segmented_regions.append(region)

# Afficher l'image avec les contours (optionnel, pour visualisation)
cv2.imshow('Contour Image', contour_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# OCR sur chaque région segmentée
for idx, region in enumerate(segmented_regions):
    # Convertir la région en texte en utilisant Tesseract
    text = pytesseract.image_to_string(region, lang='fra')  # Changer la langue si nécessaire
    
    # Afficher le texte extrait
    print(f"Texte extrait de la région {idx+1}:")
    print(text)
    print("="*30)
    