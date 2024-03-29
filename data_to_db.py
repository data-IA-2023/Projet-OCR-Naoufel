import re


    
def data_tobdd(liste,qr_code_data):
                data_todb = {}
                dico_association = {"INVOICE":"Id_Facture","Issue date":"Date"}
                liste_prod = []
                for loop in range(len(liste)):
                    for key in dico_association.keys():
                        if key in liste[loop]:
                            if key == "INVOICE":
                                data_todb[dico_association[key]] = liste[loop][8:]
                            else:
                                 data_todb[dico_association[key]] = liste[loop]
                    if loop == 2:
                        data_todb["Vendeur"] = liste[loop].split(" to ")[0]
                        data_todb["Client"] =  liste[loop].split(" to ")[1]
                    if "Address" in liste[loop]:
                        liste[loop]=liste[loop].replace("Address","")
                        data_todb["Adresse"] = " ".join([liste[loop],liste[loop+1]])
                    if "Euro" in liste[loop] and "Total" not in liste[loop]:
                        if "x" in liste[loop]:
                            if re.search(r'\d+\.\s', liste[loop]):
                                 corect_phrase = " ".join([liste[loop].split(".")[0],liste[loop].split(".",1)[1].replace('. ', '.')])
                                 liste[loop] = corect_phrase
                                 print("ok")
                            
                            # if "  "  in liste[loop]:
                            #      liste_prod.append({"Libélé_produit":liste[loop].split("  ")[0],
                            #                 "qtt":liste[loop].split("  ")[1][1],
                            #                 "prix_unitaire":(re.search(r'\d+(\.\s?\d+)?\sEuro',liste[loop].split("  ")[0])).group(0)})
                                  
                            liste_prod.append({"Libélé_produit":liste[loop].split(".")[0],
                                            "qtt":liste[loop].split(".",1)[1][1],
                                            "prix_unitaire":(re.search(r'\d+(\.\s?\d+)?\sEuro',liste[loop].split(".",1)[1])).group(0)})
                        else:
                            data_todb["Prix_Total"] = " ".join([liste[loop].split(" ")[1],liste[loop].split(" ")[2]]) 
                    data_todb["Produit"]=liste_prod
                    data_todb["Id_Client"]=qr_code_data['CUST']
                    data_todb["Catégorie"]=qr_code_data['CAT']
                    data_todb['status_request_qrcode']=qr_code_data['status_request']
                return data_todb



# def data_tobdd(liste,qr_code_data):
#     data_todb = {}
#     dico_association = {"INVOICE":"Id_Facture","Issue date":"Date"}
#     liste_prod = []
#     for loop in range(len(liste)):
#         for key in dico_association.keys():
#             if key in liste[loop]:
#                 data_todb[dico_association[key]] = liste[loop][8:]
#         if loop == 2:
#             data_todb["Vendeur"] = liste[loop].split(" to ")[0]
#             data_todb["Client"] =  liste[loop].split(" to ")[1]
#         if "Address" in liste[loop]:
#             liste[loop]=liste[loop].replace("Address","")
#             data_todb["Adresse"] = " ".join([liste[loop],liste[loop+1]])
#         if "Euro" in liste[loop] and "Total" not in liste[loop]:
#                 if "x" in liste[loop]:
#                     liste_prod.append({"Libélé_produit":liste[loop].split(".")[0],
#                                         "qtt":liste[loop].split(".",1)[1][1],
#                                         "prix_unitaire":(re.search(r'\d+(\.\s?\d+)?\sEuro',liste[loop].split(".",1)[1])).group(0)})
#                 else:
#                     data_todb["Prix_Total"] = " ".join([liste[loop].split(" ")[1],liste[loop].split(" ")[2]]) 
#         data_todb["Produit"]=liste_prod
#         data_todb["Id_Client"]=qr_code_data['CUST']
#         data_todb["Catégorie"]=qr_code_data['CAT']
#         data_todb['status_request_qrcode']=qr_code_data['status_request']
        
#             #data_todb["Adresse"].append({"Libélé_Produit":liste[loop]split(".")[0],"qtt":value,"prix_unitaire":value})



#         return data_todb
