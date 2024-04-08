import streamlit as st
import pandas as pd
from load_data import liste_fichier
from dotenv import load_dotenv
#import threading

import os
import pyodbc
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import numpy as np
# thread = threading.Thread(target=Modules.module)
# thread.start()
liste_nom = liste_fichier()
load_dotenv()

st.set_option('deprecation.showPyplotGlobalUse', False)
server = os.getenv("SQL_SERVEUR_NAME")
database = os.getenv("SQL_DB_NAME")
username = os.getenv("SQL_DB_USER")
password = os.getenv("SQL_DB_PWD")
driver = "ODBC Driver 18 for SQL Server"

connection_string = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};'
conn = pyodbc.connect(connection_string)

try:
    conn = pyodbc.connect(connection_string, driver=driver)# Connexion à la base de données
    cursor = conn.cursor() # Création d'un curseur
except Exception as e:
    erreurconnexion = f"Erreur lors de la connexion à la base de données : {e}"





file_titles = liste_fichier()

# Sidebar
selected_year = st.sidebar.selectbox("Sélectionner une année:", list(file_titles["liste_dico_fichier"].keys()))

# Récupérer la liste des fichiers pour l'année sélectionnée
files_for_selected_year = file_titles["liste_dico_fichier"].get(selected_year, [])

# Ajouter une option vide au début de la liste des fichiers
files_for_selected_year.insert(0, "")  # Ajout de la valeur vide

selected_file = st.sidebar.selectbox("Sélectionner un fichier:", files_for_selected_year)
base_url = "https://invoiceocrp3.azurewebsites.net/invoices"
if selected_file:
    # Obtenez l'URL complète du fichier sélectionné
    selected_file_url = base_url + "/" + selected_file

    # Afficher l'URL dans un iframe
    st.markdown("<h1 style='text-align: center;'>Aperçu Facture</h1>", unsafe_allow_html=True)
    st.markdown(f'<iframe src="{selected_file_url}" width="700" height="300"></iframe>', unsafe_allow_html=True)
    
    
    st.sidebar.markdown(f"[Ouvrir {selected_file.split('-')[0]}]({selected_file_url})")
# URL de base pour les fichiers (remplacez cela par votre URL de base)











SQL_SELECT_STATEMENT = "SELECT * FROM sql_db_Naoufel.dbo.Facture"

# Exécution de la requête et lecture des résultats dans un DataFrame
df_requete = pd.read_sql(SQL_SELECT_STATEMENT, conn)

SQL_SELECT_STATEMENT = "SELECT * FROM sql_db_Naoufel.dbo.Jointure"

# Exécution de la requête et lecture des résultats dans un DataFrame
df_requete1 = pd.read_sql(SQL_SELECT_STATEMENT, conn)

SQL_SELECT_STATEMENT = "SELECT * FROM sql_db_Naoufel.dbo.Client"

# Exécution de la requête et lecture des résultats dans un DataFrame
df_requete2 = pd.read_sql(SQL_SELECT_STATEMENT, conn)

SQL_SELECT_STATEMENT = "SELECT * FROM sql_db_Naoufel.dbo.Data_Récap"

# Exécution de la requête et lecture des résultats dans un DataFrame
df_requete3 = pd.read_sql(SQL_SELECT_STATEMENT, conn)

SQL_SELECT_STATEMENT = "SELECT * FROM sql_db_Naoufel.dbo.Monitoring"

# Exécution de la requête et lecture des résultats dans un DataFrame
Monitoring = pd.read_sql(SQL_SELECT_STATEMENT, conn)

SQL_SELECT_STATEMENT = "SELECT * FROM sql_db_Naoufel.dbo.Produits"

# Exécution de la requête et lecture des résultats dans un DataFrame
df_requete4 = pd.read_sql(SQL_SELECT_STATEMENT, conn)






df_requete1['Année_Facturation'] = df_requete1['ID_Facture'].str.split('_').str[1]
df_requete1.drop(["ID_Facture"], axis=1, inplace=True)
df_requete1["Quantity"]=df_requete1["Quantity"].astype(int)
df_requete[['Date_Facturation', 'Heure_Facturation']] = df_requete['Date'].apply(lambda x: pd.Series(x.split(' ')))
df_requete['Année_Facturation'] = df_requete['Date_Facturation'].apply(lambda x: x[0:4])
df_requete['Année_Facturation'] = df_requete['Année_Facturation'].replace("019-", "2019")
df_requete['Année_Facturation'] = df_requete['Année_Facturation'].replace("020-", "2020")
df_requete['Année_Facturation'] = df_requete['Année_Facturation'].replace("021-", "2021")
df_requete['Année_Facturation'] = df_requete['Année_Facturation'].replace("022-", "2022")
df_requete['Année_Facturation'] = df_requete['Année_Facturation'].replace("023-", "2023")
df_requete['Année_Facturation'] = df_requete['Année_Facturation'].replace("024-", "2024")
df_requete['Année_Facturation'] = df_requete['Année_Facturation'].astype(float)
df_requete['Prix_Total'] = df_requete['Prix_Total'].astype(float)




def graph(df_requete,df_requete1):
    
    warnings.filterwarnings("ignore", category=UserWarning)
    
    #######1
    ventes_par_annee = df_requete.groupby('Année_Facturation')['Prix_Total'].sum()
    ventes_par_annee = ventes_par_annee.reset_index()   
   
    

    # Nombre de factures par année
    
    plt.title("Nombre de Facture par année")
    sns.countplot(data=df_requete, x='Année_Facturation',palette="Set1")
    st.pyplot()

    # Total des ventes par année
    
    plt.title("Total des ventes par année")
    sns.barplot(data=ventes_par_annee, x='Année_Facturation', y='Prix_Total',palette="Set1")
    plt.xlabel("Année")
    plt.ylabel("Prix Total (en Millions d'euros)")
    st.pyplot()
    
    
    #######2
    df_requete1ordered = df_requete1.sort_values(by='Quantity',ascending=False)
    plt.title("Total des meilleurs ventes")
    sns.barplot(data=df_requete1ordered.head(10), x='Libellé_Produit', y='Quantity',palette="Set1")
    plt.xlabel("Produit")
    plt.ylabel("Quantity")
    max_quantity = df_requete1ordered['Quantity'].max()
    plt.ylim(0, max_quantity /50)
    plt.xticks(rotation=45,fontsize=8,ha='right')
    st.pyplot()
   
    
    ###########3
    
    
    df_aggregated = df_requete1.groupby(['Libellé_Produit', 'Année_Facturation'], as_index=False)['Quantity'].sum()
    df_filtered = df_aggregated[df_aggregated['Libellé_Produit'] != 'Inconnu']
    df_sorted = df_filtered.sort_values(by=['Année_Facturation', 'Quantity'], ascending=[True, False])
    
    # Définir une fonction pour sélectionner les trois premiers produits par groupe
    def top_three(group):
        return group.head(3)

    # Appliquer la fonction à chaque groupe
    top_products = df_sorted.groupby('Année_Facturation').apply(top_three)

    # Réinitialiser l'index
    top_products = top_products.reset_index(drop=True)
    st.write(top_products)

    ##################4


    # Tracé du graphique
    plt.title("Nombre de Clients par Catégorie")
    sns.countplot(x=df_requete2["Catégorie"], palette="Set1")  # Utilisation de la palette "Set3" pour les couleurs
    plt.xlabel("Catégorie Client")
    plt.ylabel("Nombre de Clients")
    st.pyplot()
    
    return
print(df_requete4['Libellé_Produit'].nunique())
def graphmonitoring(df):
    nombre_de_facture = len(df)
   
    plt.figure(figsize=(6, 4))
    plt.bar( "Nombre de Factures",nombre_de_facture)
    plt.title('Nombre total de factures')
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()
    st.pyplot()
    

    occurrences = df["status_load_data"].value_counts()
    plt.figure(figsize=(8, 6))
    occurrences.plot(kind='bar')
    plt.ylabel('Occurrences')
    plt.title('Occurrences de chaque valeur dans la colonne status_load_data')
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()
    st.pyplot()

    occurrences = df["SELECT_Produit"].value_counts()
    plt.figure(figsize=(8, 6))
    occurrences.plot(kind='bar')
    plt.ylabel('Occurrences')
    plt.title('Occurrences de chaque valeur dans la colonne SELECT_Produit')
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()
    st.pyplot()

    
    df2 = df
    df2['INSERT_Produit'] = df2['INSERT_Produit'].apply(lambda x: 'erreur' if x not in ['Le produit avait déjà été renseigné', 'La requête INSERT a été exécutée avec succès.'] else x)

    occurrences = df2["INSERT_Produit"].value_counts()
    st.write(occurrences)
    plt.figure(figsize=(8, 6))
    occurrences.plot(kind='bar')
    plt.ylabel('Occurrences')
    plt.title('Occurrences de chaque valeur dans la colonne INSERT_Produit')
    plt.xticks(rotation=55)  # Rotation des étiquettes de l'axe x pour éviter le chevauchement
    plt.tight_layout()
    plt.show()
    st.pyplot()

   
    df2 = df
    df2['INSERT_Jointure'] = df2['INSERT_Jointure'].apply(lambda x: 'erreur' if x not in ['La requête INSERT a été exécutée avec succès.'] else x)

    occurrences = df2["INSERT_Jointure"].value_counts()
    st.write(occurrences)
    plt.figure(figsize=(8, 6))
    occurrences.plot(kind='bar')
    plt.ylabel('Occurrences')
    plt.title('Occurrences de chaque valeur dans la colonne INSERT_Jointure')
    plt.xticks(rotation=55) # Rotation des étiquettes de l'axe x pour éviter le chevauchement
    plt.tight_layout()
    plt.show()
    st.pyplot()

   
    









option = st.sidebar.selectbox(
    'Que souhaitez-vous afficher?',
    ('', 'Données', 'Graphiques',"Monitoring")
)

# Afficher le graphique correspondant à l'option sélectionnée
if option == 'Données':
    st.markdown("<h1 style='text-align: center;'>Récapitulatif des données</h1>", unsafe_allow_html=True)
    st.write(df_requete3)
elif option == 'Graphiques':
    st.markdown("<h1 style='text-align: center;'>Graphiques des données</h1>", unsafe_allow_html=True)
    graph(df_requete,df_requete1)  
elif option == 'Monitoring':
    st.markdown("<h1 style='text-align: center;'>Monitoring</h1>", unsafe_allow_html=True)
    st.write(Monitoring)
    graphmonitoring(Monitoring)

cursor.close()
conn.close()

