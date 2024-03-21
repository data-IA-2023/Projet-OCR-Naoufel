from dotenv import load_dotenv
import requests,os
import pandas as pd
from AzurComputerVivsion import OCR
from load_data import rechercheNom,année
import datetime





liste , status , url,dico = année(2022) 
print(dico.keys(),dico)

OCR(dico,url)


"""

while True:
    try:
        liste , status , url = année(year) 
    except:
        print()
        
"""           


"https://invoiceocrp3.azurewebsites.net/invoices/FAC_2022_0001-190575.png"








"""
OCR()
for nom_image in liste:






#telecharger_images(liste,url)

#OCR(url)
"""