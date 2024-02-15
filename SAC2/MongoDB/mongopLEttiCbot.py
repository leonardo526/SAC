import pymysql
from pymongo import MongoClient

# Connessione al database MySQL
mysql_connection = pymysql.connect(
    host='localhost',
    user='username',
    password='password',
    database='daitv12'
)

# Connessione al database MongoDB
mongo_client = MongoClient('mongodb://localhost:27017/')
mongo_db = mongo_client['daitatv']
mongo_collection = mongo_db['queries']

try:
    with mysql_connection.cursor() as cursor:
        # Esempio di query per selezionare dati da una tabella MySQL
        sql_query = """SELECT generi.Genere, COUNT(generirel.FilmID) FROM `generi`
                    JOIN generirel ON generi.GenreID = generirel.GenreID
                    GROUP BY generirel.GenreID;"""

        cursor.execute(sql_query)
        result = cursor.fetchall()

        # Inserimento dei dati nella collezione MongoDB
        for row in result:
           mongo_collection.insert_one(row)

    print("Dati inseriti con successo in MongoDB")

finally:
    mysql_connection.close()
    mongo_client.close()