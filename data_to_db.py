import re
import math

    
def data_tobdd(liste,qr_code_data):
                """
                Fonction qui effectue du prétraitement sur la réponse de l'OCR afin d'identifier les différentes informations 
                Il en ressort un dictionnaire comprenant les données
                INPUT: liste(resultat de l'OCR,qr_code_data(les données du qrcode))
                OUTPUT: data_bdd(dictionnaire contenant toutes les données)
                """
                data_todb = {}
                dico_association = {"INVOICE":"Id_Facture","Issue date":"Date","issue date":"Date"}
                liste_prod = []
                for loop in range(len(liste)):
                    for key in dico_association.keys():
                        if key in liste[loop]:
                            if key == "INVOICE":
                                data_todb[dico_association[key]] = liste[loop][8:]
                            elif key == "Issue date":
                                 data_todb[dico_association[key]] = liste[loop][11:]
                            else:
                                 data_todb[dico_association[key]] = liste[loop][11:]

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

def rempalcement0(dico):
    """
    Fonction qui effectue du prétraitement pour remplacer les valeurs manquantes déja indentifiées dans la fonction précedante 
    Il en ressort un dictionnaire 
    INPUT: dico(OUTPUT de la fonction précédante)
    OUTPUT: dictionnaire modifé
    """
    listeprix = []
    count = 0

    for i, produit in enumerate(dico["Produit"]):
        if produit["qtt"] == "0" or produit["qtt"] == "x" :
            prixunit = float(produit["prix_unitaire"].split(" ")[0])
            count = 1
            index = i
        else:
            operation = float(produit["qtt"]) * float(produit["prix_unitaire"].split(" ")[0])
            listeprix.append(operation)

    if count == 1:
        remaining_total = float(dico["Prix_Total"].split(" ")[0]) - round(sum(listeprix), 2)
        qtt_decimal = remaining_total / prixunit
        if qtt_decimal - math.floor(qtt_decimal) >= 0.5:
            dico['Produit'][index]['qtt'] = math.ceil(qtt_decimal)
        else:
            dico['Produit'][index]['qtt'] = math.floor(qtt_decimal)

    return dico



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