from pymongo import MongoClient
from dbUtils import *
""" 
sys.path.append('create db')
from dbUtils import *
# prima non funzionava perche non c'era un file __init__.py in create db  
"""


conString = "mongodb://localhost:27017"

client = MongoClient(conString)
daitv12 = client.daitv12
film = daitv12.film
generi = daitv12.generi
utenti = daitv12.utenti
generirel = daitv12.generirel
rating = daitv12.rating

c = create_db_connection("daitv12")
lista_film = read_query(c,"SELECT * FROM film")
lista_generi = read_query(c, "SELECT * FROM generi")
lista_utenti = read_query(c, "SELECT * FROM utenti")
lista_generi_rel = read_query(c, "SELECT * FROM generirel")
lista_rating = read_query(c, "SELECT * FROM rating")

film.insert_many(lista_film)
generi.insert_many(lista_generi)
utenti.insert_many(lista_utenti)
generirel.insert_many(lista_generi_rel)
rating.insert_many(lista_rating)

client.close()