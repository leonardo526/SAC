from pymongo import MongoClient
from dbUtils import *
import pandas as pd
import statistics
""" 
sys.path.append('create db')
from dbUtils import *
# prima non funzionava perche non c'era un file __init__.py in create db  
"""
df_film = pd.read_csv(r'C:\Users\Utente\PycharmProjects\pythonProjectSql\SAC\SAC2\create db\New_Elenco_Movies_Pulito.csv')
df_rating = pd.read_csv(r'C:\Users\Utente\PycharmProjects\pythonProjectSql\SAC\SAC2\create db\ratings_edit.csv')
df_film_rating = pd.merge(df_film, df_rating['Rating'], on='MovieID', how='left')
df_film_rating['Rating'] = df_film_rating['Rating'].groupby('MovieID')['Rating'].transform(lambda x: statistics.mean(x))
df_utenti = pd.read_csv(r'C:\Users\Utente\PycharmProjects\pythonProjectSql\SAC\SAC2\create db\users_edit.csv')
df_utenti_rating = pd.merge(df_utenti,df_rating['Rating'], on='UserID', how='left')
df_utenti_rating['Rating'] = df_utenti_rating['Rating'].groupby('UserID')['Rating'].transform(lambda x: ', '.join(x))

film_dict = df_film_rating.to_dict(orient='records')
utenti_dict = df_utenti_rating.to_dict(orient='records')
# conString = "mongodb://localhost:27017"
#
# client = MongoClient(conString)
# daitv12 = client.daitv12
# film = daitv12.film
# utenti = daitv12.utenti
#
# film.insert_many(film_dict)
# utenti.insert_many(utenti_dict)
#
#
# # --QUERY--
# # Numero di film per anno
# q1 = film.aggregate([{"$group" : {_id:"Year", count:{"Title"}}}])
# for x in q1:
#     print(x)
#
# # Il numero di film per ogni genere
#
# q2 =
#
# # I film che hanno recensioni al di sotto di 3 per un numero 250 di persone in modo da eliminarli
# # La top 10 per ogni intervallo di età e sesso
# # Rating film - i voti dal meno preferito al più preferito per fasce di età
# # Il numero degli iscritti alla piattaforma nelle varie province, voglio vedere le prime 20
# # Il numero degli abbonati in base al lavoro
# client.close()