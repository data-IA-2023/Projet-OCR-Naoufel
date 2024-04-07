

from AzurComputerVivsion import OCR
from load_data import liste_fichier
from data_to_db import data_tobdd
from data_to_db import rempalcement0
from BDD import requetes_sql
from requetes import select
from DiscordMonitoring import discord


def module():
    dico_nom_fichier = liste_fichier()
    #reversed() : dico_nom_fichier['liste_dico_fichier'].keys()
    for année in dico_nom_fichier['liste_dico_fichier'].keys():
        for titre in dico_nom_fichier['liste_dico_fichier'][année]:
            result_list,Status_SELECT_redondance = select("Monitoring","ID_Facture")
            result_listfac,Status_SELECT_redondancefac = select("Facture","ID_Facture")
            
            if titre.split("-")[0] not in result_list or titre.split("-")[0] not in result_listfac:
                # print(titre.split("-")[0])
                try:
                    DICO_OCR = OCR(titre)
                except Exception as e:
                    status_text_to_ocr = f"Erreur lors de l'OCR sur les données {titre.split("-")[0]}'  : {e}"
                else:
                    status_text_to_ocr = "OCR terminé"

                
            
                    
                try:   
                    DICO_DB = data_tobdd(DICO_OCR["liste"],DICO_OCR["qr_code_data"])
                    
                    
                    DICO_FINAL = rempalcement0(DICO_DB)
                except Exception as e:
                    status_processing_ocr = f"Erreur lors de la requête INSERT à la base de données  : {e}"
                else:
                    status_processing_ocr = "Préprocessing terminé"

                
                DICO_STATUS2 = {"status_load_data":dico_nom_fichier["status_laod_data"],
                                "status_SELECT_redondance":Status_SELECT_redondance,
                                "status_text_to_ocr":status_text_to_ocr,
                                "status_processing_ocr":status_processing_ocr
                                }
                # print(DICO_DB)
                # print(DICO_FINAL)
                DICO_STATUS = requetes_sql(DICO_FINAL,DICO_STATUS2)
                print(f"------------------------------------------------------{DICO_FINAL["Id_Facture"]}------------------------------------------------------------------")
                discord(DICO_STATUS,DICO_STATUS2)
            else:
                status_processing_ocr = "Le fichier a déjà été renseigné"
                print("Le fichier a déjà été renseigné")
    return
module()

    
        
        
    
  
    
                   
    
                   










    # for element in DICO_DB["Produit"]:
    #     produit = float(element["qtt"])*float(element["prix_unitaire"].split(" ")[0])
    #     listeprix.append(produit)
    #     # print("qtt",element['qtt'])
    #     # print("prix",element['prix_unitaire'].split(" ")[0])
    #     # print('prod',float(element["qtt"])*float(element["prix_unitaire"].split(" ")[0]))
    #     # print("prixtotal",round(float(DICO_DB["Prix_Total"].split(" ")[0])))
    #     if element['qtt']== "0":
    #         element['qtt']=round(float(DICO_DB["Prix_Total"].split(" ")[0])-round(sum(listeprix)))/float(element["prix_unitaire"].split(" ")[0])
    #         print("new",element['qtt'])
    #         print("------------------------------houra----------------------------------")                
    #   print("1",float(produit["qtt"]))
    #   print("2",float(produit["prix_unitaire"].split(" ")[0]))
              
              
              
        
    




    # if sum(listeprix) == (DICO_DB["Prix_Total"]


        






