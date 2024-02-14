import pandas as pd
from dbUtils import *

c = create_db_connection("Daitv12")
df = pd.read_csv("ratings_edit.csv")
lista_upload = []
for x in df.to_dict(orient="records"):
    lista_upload.append((x['UserID'],x['MovieID'],x['Rating'], x['Timestamp']))

q = "INSERT INTO rating(UserID, FilmID, Rating, Timestamp) VALUES(%s, %s, %s, %s)"
execute_many_query(c,q, lista_upload)