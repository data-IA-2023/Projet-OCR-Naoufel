

from AzurComputerVivsion import OCR
from load_data import liste_fichier
from data_to_db import data_tobdd


dico_nom_fichier = liste_fichier()


#for année in dico_nom_fichier['liste_dico_fichier'].keys():
for titre in dico_nom_fichier['liste_dico_fichier'][2019]:
    DICO_OCR = OCR(titre)
    # print(DICO_OCR)
    
    DICO_DB = data_tobdd(DICO_OCR["liste"],DICO_OCR["qr_code_data"])
    print(DICO_DB)
    # print(DICO_OCR["liste"])
    # print(DICO_DB["Produit"])
    # print("total",DICO_DB["Prix_Total"].split(" ")[0])
    listeprix=[]
    count = 0

    
    for produit in DICO_DB["Produit"]:
            if produit["qtt"] == "0":
                count = 1
                
                
            else:
                produit = float(produit["qtt"])*float(produit["prix_unitaire"].split(" ")[0])
                listeprix.append(produit)
    if count == 1:
         produit['qtt']=round(float(DICO_DB["Prix_Total"].split(" ")[0])-round(sum(listeprix)))/float(element["prix_unitaire"].split(" ")[0])
         print(" ------------------CHANGEMENT---------------")
    print("-----------------------------------PRODUIT FINI-------------------------")
    print(DICO_DB)
    
    
                   
    
                   
                   
    """for element in DICO_DB["Produit"]:
        produit = float(element["qtt"])*float(element["prix_unitaire"].split(" ")[0])
        listeprix.append(produit)
        # print("qtt",element['qtt'])
        # print("prix",element['prix_unitaire'].split(" ")[0])
        # print('prod',float(element["qtt"])*float(element["prix_unitaire"].split(" ")[0]))
        # print("prixtotal",round(float(DICO_DB["Prix_Total"].split(" ")[0])))
        if element['qtt']== "0":
            element['qtt']=round(float(DICO_DB["Prix_Total"].split(" ")[0])-round(sum(listeprix)))/float(element["prix_unitaire"].split(" ")[0])
            print("new",element['qtt'])
            print("------------------------------houra----------------------------------")"""                   
            #   print("1",float(produit["qtt"]))
            #   print("2",float(produit["prix_unitaire"].split(" ")[0]))
              
              
              
        
    




    # if sum(listeprix) == (DICO_DB["Prix_Total"]


        






