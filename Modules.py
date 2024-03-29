

from AzurComputerVivsion import OCR
from load_data import liste_fichier
from data_to_db import data_tobdd


dico_nom_fichier = liste_fichier()


#for année in dico_nom_fichier['liste_dico_fichier'].keys():
for titre in dico_nom_fichier['liste_dico_fichier'][2019]:
    DICO_OCR = OCR(titre)
    
    DICO_DB = data_tobdd(DICO_OCR["liste"],DICO_OCR["qr_code_data"])
    print(DICO_OCR["liste"])
    print(DICO_DB["Produit"])
    print("total",DICO_DB["Prix_Total"].split(" ")[0])
    listeprix=[]
    for produit in DICO_DB["Produit"]:
        print("1",float(produit["qtt"]))
        print("2",float(produit["prix_unitaire"].split(" ")[0]))
        produit = float(produit["qtt"])*float(produit["prix_unitaire"].split(" ")[0])
        print("produit",produit)
        listeprix.append(produit)
    print("listeprix",sum(listeprix))




    # if sum(listeprix) == (DICO_DB["Prix_Total"]


        






