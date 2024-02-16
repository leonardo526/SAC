import pandas as pd
from dbUtils import *

c = create_db_connection("Daitv12")
df = pd.read_csv("ratings_edit.csv")
lista_upload= []
for x in df.to_dict(orient="records"):
    lista_upload.append((x['UserID'],x['MovieID'],x['Rating'], x['Timestamp']))
lista_upload1 = lista_upload[:len(lista_upload)//50]
# lista_upload2 = lista_upload[len(lista_upload)//2:]
q = "INSERT INTO rating(UserID, FilmID, Rating, Timestamp) VALUES(%s, %s, %s, %s)"
# cursor = c.cursor()
# a = 1
# for elem in lista_upload:
#     cursor.execute(q, elem)
#     print(a)
#     a+=1

# c.commit()
execute_many_query(c,q,lista_upload1)
