
#Importando Libreria mysql.connector para conectar Python con MySQL
import mysql.connector

def connectionBD():
    mydb = mysql.connector.connect(
        host ="database-1-php.cwz8u6oh3k3m.us-east-1.rds.amazonaws.com",
        user ="admin",
        passwd ="metabee1rokusho",
        database = "empresax"
        )
    if mydb:
        print ("Conexion exitosa")
    else:
        print ("Error en la conexion a BD")
    return mydb
     