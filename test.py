"""dico = {'Id_Facture': 'FAC_2019_0038', 'Produit': [{'Libélé_produit': 'Likely partner area building', 'qtt': '3', 'prix_unitaire': '22.55 Euro'}, {'Libélé_produit': 'Tout connaître bruit rappeler', 'qtt': '6', 'prix_unitaire': '31.96 Euro'}, {'Libélé_produit': 'Beaucoup propre révolution douceur', 'qtt': '1', 'prix_unitaire': '54.39 Euro'}, {'Libélé_produit': 'Inconnu', 'qtt': '1', 'prix_unitaire': '62.34 Euro'}, {'Libélé_produit': 'Ullam quibusdam repellendus fuga', 'qtt': "0", 'prix_unitaire': '8.38 Euro'}, {'Libélé_produit': 'Avancer train avec plaine', 'qtt': '5', 'prix_unitaire': '24.07 Euro'}, {'Libélé_produit': 'Molestias natus possimus nostrum', 'qtt': '7', 'prix_unitaire': '35.70 Euro'}, {'Libélé_produit': 'Début raconter sorte militaire', 'qtt': '5', 'prix_unitaire': '5.87 Euro'}], 'Id_Client': '00432', 'Catégorie': 'C', 'status_request_qrcode': 200, 'Date': 'Issue date 2019-01-13 02:10:00', 'Vendeur': 'Bill', 'Client': 'Anouk Pires', 'Adresse': ' 82780 Jason Track Wendymouth, IN 28463', 'Prix_Total': '800.88 Euro'}
import math
listeprix = []
count = 0

for i, produit in enumerate(dico["Produit"]):
    if produit["qtt"] == "0":
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

print(dico)

print(dico)"""
import streamlit as st
liste=[1,2,6,9]
print(str(liste))
st.write("yolo")
def count():
    a = 0
    for loop in range(100000000000):
        a += loop
    return a
count()
