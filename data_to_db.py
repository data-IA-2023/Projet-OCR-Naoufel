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
                    if "TOTAL" in liste[loop]:
                        #   print("total",liste[loop])
                          data_todb["Prix_Total"] = " ".join([liste[loop].split(" ")[1],liste[loop].split(" ")[2]])
                    elif "Euro" in liste[loop]:
                        # print("euro",liste[loop])
                        if "  " in liste[loop]:
                                liste[loop] = liste[loop].replace('  ', '. ')
                        if re.search(r'\d{2}\. \d{2}', liste[loop]):
                                # print("ok")
                                # print(liste[loop])
                                # print("Libélé_produit",liste[loop].split(".")[0])
                                # print("qtt",liste[loop].split(".",1)[1][1])
                                # print("prix_unitaire",(re.search(r'\d+(\.\s?\d+)?\sEuro',liste[loop].split(".",1)[1])).group(0))
                                # print("phrase avant: ",liste[loop])
                                liste[loop] =re.sub(r'\. (\d+)', r'.\1', liste[loop])
                                liste[loop] =re.sub(r'([a-zA-Z])\.(\d+)', r'\1. \2',liste[loop])
                                # print("phrase après: ",liste[loop])  
                        if len(liste[loop]) <15:
                               liste[loop] = f"Inconnu. {liste[loop]}"
                        if re.search(r'\bX\s+(\d+\.\d+\s+Euro)\b',liste[loop]):
                              liste[loop] = re.sub(r'\bX\s+(\d+\.\d+\s+Euro)\b', r'0 x \1', liste[loop])
                            #   print("why not")
                             
                              
                              
                    
                        liste_prod.append({"Libélé_produit":liste[loop].split(".")[0],
                                            "qtt":liste[loop].split(".",1)[1][1],
                                            "prix_unitaire":(re.search(r'\d+(\.\s?\d+)?\sEuro',liste[loop].split(".",1)[1])).group(0)})
                        
                    
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



 # if re.search(r'\d+\.\s+\d+', liste[loop]):
                                #  corect_phrase = " ".join([liste[loop].split(".")[0],(liste[loop].split(".",1)[1]).replace('. ', '.')])
                                #  print("dedans",liste[loop].split(".")[0],"/",liste[loop].split(".",1)[1])
                                #  liste[loop] = corect_phrase
                                #  print("listeloppop",liste[loop])
                                #  print("ok")
                            #print("dehors")
                            
                            # if "  "  in liste[loop]:
                            #      liste_prod.append({"Libélé_produit":liste[loop].split("  ")[0],
                            #                 "qtt":liste[loop].split("  ")[1][1],
                            #                 "prix_unitaire":(re.search(r'\d+(\.\s?\d+)?\sEuro',liste[loop].split("  ")[0])).group(0)})