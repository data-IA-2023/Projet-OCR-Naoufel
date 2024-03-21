
import pandas as pd
from AzurComputerVivsion import OCR
from load_data import année






liste , status , url,dico = année(2023) 


dico_ocr = OCR(dico,url)
print(dico_ocr.keys())

listequantité=[]
listenom=[]
listedate=[]
listeprix=[]
listeproduits=[]

for key in dico_ocr.keys():
    row=dico_ocr[key]
    listenom.append(row[0])
    listedate.append(row[1])
    listeprix.append(row[-1])
    listeproduits.append(row[-3])
    listequantité.append(row[-4])
    
df= pd.DataFrame({     "Nom_Facture":listenom,
                      "Date_Facture":listedate,
                      "Total_Facture":listeprix,
                      "Produces":listeproduits,
                      "Quantité":listequantité
                 

                  },index=dico_ocr.keys())


print(df)







"""
while True:
    try:
        liste , status , url = année(year) 
    except:
        print()
"https://invoiceocrp3.azurewebsites.net/invoices/FAC_2022_0001-190575.png"
OCR()
for nom_image in liste:
#telecharger_images(liste,url)
#OCR(url)
"""