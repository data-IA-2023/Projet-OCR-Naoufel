import streamlit as st


#import  Modules 
#Environnement
from Modules import dico_nom_fichier
from dotenv import load_dotenv
import os

import threading
#Requetes SQL
import pyodbc

import pandas as pd

# thread = threading.Thread(target=Modules.module)
# thread.start()

load_dotenv()


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




SQL_SELECT_STATEMENT = "SELECT ID_Facture FROM sql_db_Naoufel.dbo.Facture"

# Exécution de la requête et lecture des résultats dans un DataFrame
df = pd.read_sql(SQL_SELECT_STATEMENT, conn)

# Afficher le DataFrame
print(df)
st.sidebar.write(df)
st.write(dico_nom_fichier['liste_dico_fichier'])

