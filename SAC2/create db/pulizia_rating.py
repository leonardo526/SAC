import pandas as pd
from dbUtils import *

c = create_db_connection("utenti")
df = pd.read_csv("ratings_edit.csv")

df2 = pd.read_csv("New_Elenco_Movies_Pulito.csv")

lista_id_film = []

for x in df2.to_dict(orient="records"):
    id_db = read_query(c,f"""SELECT FilmID FROM film WHERE Title = "{x['Title']}" """)
    if id_db != None:
        id_db = id_db[0]['FilmID']
        lista_id_film.append((x['MovieID'], id_db))


lista_upload = []
for x in df.to_dict(orient="records"):
    for y in lista_id_film:
        if y[0] == x['MovieID']:
            lista_upload.append((x['UserID'],y[1],x['Rating'], x['Timestamp']))

q = "INSERT INTO rating(UserID, FilmID, Rating, Timestamp) VALUES(%s, %s, %s, %s)"
execute_many_query(c,q, lista_upload)