from connectionstr import cursor
def select(table,colomn):
        try:
            SQL_SELECT_STATEMENT = f"""SELECT {colomn} FROM sql_db_Naoufel.dbo.{table}"""
            cursor.execute(SQL_SELECT_STATEMENT)
            rows = cursor.fetchall()

            result_list = []

            result_list = [row[0] for row in rows]
            message ="La requête SELECT a été exécutée avec succès." 
            return result_list,message
            

        except Exception as e:
            return(f"Erreur lors de la requête SELECT : {e}")
        
            
        


