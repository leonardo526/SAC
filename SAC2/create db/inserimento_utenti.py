import pandas as pd
from dbUtils import *

df = pd.read_csv("new_users_edit.csv")
lista=[]
for x in df.to_dict(orient="records"):
    lista.append((x["UserID"],x['Gender'],x['Age'],x['CAP'],x['Work'],))
c = create_db_connection('utenti')
q = f"""INSERT INTO utenti (UserID,Gender,Age,CAP,Work) VALUES("{x['UserID']}","{x['Gender']}","{x['Age']}","{x['CAP']}","{x['Work']}")"""

execute_many_query(c,q,lista)


