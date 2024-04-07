# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 08:59:55 2024

@author: naouf
"""

#Environnement
from dotenv import load_dotenv
import os
from requetes import select

#Requetes SQL
import pyodbc

#Requetes SQL
import pyodbc







def requetes_sql(dico,DICO_STATUS2):
    """
    Fonction qui prend comme parametres les dictionnaires de monitoring de l'ocr et dautre fonctions ainsi que le dictionnaire final contenant les données
    et les envois sur différentes tables de la base donnée dédiée
    Il en ressort un dictionnaire de monitoring des requetes vers la base de données.
    INPUT: dico1,DICO_STATUS2
    OUTPUT: DICO_STATUS
    """


    #Connexion base de données
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
        statusConnexionBDD = f"Erreur lors de la connexion à la base de données : {e}"
    else:
       statusConnexionBDD = "La connexion à la base a été exécutée avec succès."


    # print("-------------------------Facture-------------------------------")
    #select pour verifier le contenue de ma table , deuxieme hitération
    result_list,Status_SELECT_Facture = select("Facture","ID_Facture")
    # print("-------------------------Client-------------------------------")
    result_list,Status_SELECT_Client = select("Client","ID_Client")
    if dico["Id_Client"] not in result_list:
        try:
            # Exécution d'une requête SQL
            SQL_INSERT_STATEMENT = """
            INSERT into sql_db_Naoufel.dbo.Client (
            Name, 
            Adresse,
            ID_Client, 
            Catégorie
            )
            VALUES (?,?,?,?)
            """
            
        
            cursor.execute(SQL_INSERT_STATEMENT,dico["Client"],dico["Adresse"],dico["Id_Client"],dico["Catégorie"])
        
            
            conn.commit()

        except Exception as e:
             status_INSERT_Client = f"Erreur lors de la requête INSERT à la base de données  : {e}"
        
        else:
            status_INSERT_Client = "La requête INSERT a été exécutée avec succès."
    else:
         status_INSERT_Client = "Le client avait déjà été renseigné"



    #meme shema pour les autres tables
    #Si ma table ne contient pas mon titre de document , je commence a envoyer mes données
    if dico["Id_Facture"] not in result_list:
        try:
            # Exécution d'une requête SQL
            SQL_INSERT_STATEMENT = """
            INSERT into sql_db_Naoufel.dbo.Facture (
            ID_Facture, 
            Date, 
            Prix_Total,
            ID_Client
            )
            VALUES (?,?,?,?)
            """
            
            
            cursor.execute(SQL_INSERT_STATEMENT,dico["Id_Facture"],dico["Date"],dico["Prix_Total"].split(" ")[0],dico["Id_Client"])
            
        
            
            conn.commit()

        except Exception as e:
            status_INSERT_Facture = f"Erreur lors de la requête INSERT à la base de données  : {e}"
        else:
            status_INSERT_Facture = "La requête INSERT a été exécutée avec succès. "
    else:
         status_INSERT_Facture = "La facture avait déjà été renseignée "


    
    




    # print("-------------------------Produit-------------------------------")
    result_list,Status_SELECT_Produit = select("Produits","Libellé_Produit")
    
    try:
        for element in dico["Produit"]:
            if element["Libélé_produit"] not in result_list:
                
                    # Exécution d'une requête SQL
                    SQL_INSERT_STATEMENT = """
                    INSERT into sql_db_Naoufel.dbo.Produits (
                    Libellé_Produit, 
                    Prix_Produit
                    )
                    VALUES (?,?)
                    """
                    
                
                    cursor.execute(SQL_INSERT_STATEMENT,element["Libélé_produit"],element["prix_unitaire"].split(" ")[0])
                
                    
                    conn.commit()
                    status_INSERT_Produit ="La requête INSERT a été exécutée avec succès."
            else:
                status_INSERT_Produit = "Le produit avait déjà été renseigné"

    except Exception as e:
        status_INSERT_Produit =f"Erreur lors de la requête INSERT à la base de données  : {e}"
        

   


    # print("-------------------------Jointure-------------------------------")
    result_list,Status_SELECT_Jointure = select("Jointure","ID_Facture")
    result_list_prod,Status_SELECT_Jointure_prod = select("Jointure","Libellé_Produit")
    try:
        for element in dico["Produit"]:
            
            if dico["Id_Facture"] not in result_list:
                    # Exécution d'une requête SQL
                    SQL_INSERT_STATEMENT = """
                    INSERT into sql_db_Naoufel.dbo.Jointure (
                    ID_Facture,
                    Libellé_Produit, 
                    Quantity
                    )
                    VALUES (?,?,?)
                    """
                    
                
                    cursor.execute(SQL_INSERT_STATEMENT,dico["Id_Facture"],element["Libélé_produit"],element["qtt"])
                
                    
                    conn.commit()
                    status_INSERT_Jointure = "La requête INSERT a été exécutée avec succès."
            else:
                status_INSERT_Jointure = "La jointure avait déjà étée renseignée"

    except Exception as e:
        status_INSERT_Jointure = f"Erreur lors de la requête INSERT à la base de données  : {e}"
        
   
    
    

    
    DICO_STATUS = {"connexion":statusConnexionBDD,
                   "SELECT_Facture":Status_SELECT_Facture,
                   "INSERT_Facture":status_INSERT_Facture,
                   "SELECT_Client":Status_SELECT_Client,
                   "INSERT_Client":status_INSERT_Client,
                   "SELECT_Produit":Status_SELECT_Produit,
                   "INSERT_Produit":status_INSERT_Produit,
                   "SELECT_Jointure":Status_SELECT_Jointure,
                   "INSERT_Jointure":status_INSERT_Jointure}
    
    
    
    result_list,Status_SELECT_monitoring = select("Monitoring","ID_Facture")
    if dico["Id_Facture"] not in result_list:

        SQL_INSERT_STATEMENT = """
                        INSERT into sql_db_Naoufel.dbo.Monitoring (
                        ID_Facture,
                        status_load_data,
                        status_SELECT_redondance, 
                        status_text_to_ocr,
                        status_processing_ocr,
                        connexion,
                        SELECT_Facture,
                        INSERT_Facture,
                        SELECT_Client,
                        INSERT_Client,
                        SELECT_Produit,
                        INSERT_Produit,
                        SELECT_Jointure,
                        INSERT_Jointure,
                        date_heure
                        )
                        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,CURRENT_TIMESTAMP)
                        """
                        
                    
        cursor.execute(SQL_INSERT_STATEMENT, dico["Id_Facture"], DICO_STATUS2["status_load_data"], DICO_STATUS2["status_SELECT_redondance"], DICO_STATUS2["status_text_to_ocr"], DICO_STATUS2["status_processing_ocr"], DICO_STATUS["connexion"], DICO_STATUS["SELECT_Facture"], DICO_STATUS["INSERT_Facture"], DICO_STATUS["SELECT_Client"], DICO_STATUS["INSERT_Client"], DICO_STATUS["SELECT_Produit"], DICO_STATUS["INSERT_Produit"], DICO_STATUS["SELECT_Jointure"], DICO_STATUS["INSERT_Jointure"])
                    
                        
        conn.commit()
    


    #fermeture du cursor et de la connexion
    cursor.close()
    conn.close()
    return DICO_STATUS

    # try:
    #     # Exécution d'une requête SQL
    #     SQL_STATEMENT = """
    #     INSERT into sql_db_Naoufel.dbo.Client (
    #     Name, 
    #     Adresse, 
    #     ID_Client,
    #     Catégorie
    #     )
    #     VALUES (?,?,?,?)
    #     """
    
    #     cursor.execute(SQL_STATEMENT,dico["Client"],dico["Adresse"],dico["Id_Client"],dico["Catégorie"])
    
        
    #     conn.commit()

    # except Exception as e:
    #     print(f"Erreur lors de la connexion à la base de données : {e}")
    # else:
    #     print("La requête a été exécutée avec succès.")
    
        # Fermeture du curseur et de la connexion
