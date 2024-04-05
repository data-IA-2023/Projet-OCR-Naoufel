from dotenv import load_dotenv
import os


#Requetes SQL
import pyodbc


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
    print(f"Erreur lors de la connexion à la base de données : {e}")
else:
    print("La connexion à la base a été exécutée avec succès.")