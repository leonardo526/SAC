import pandas as pd
from dbUtils import *

df = pd.read_csv("new_users_edit.csv")
df2 = pd.read_csv("caprovince.csv", delimiter= ";")
lista=[]
for x in df.to_dict(orient="records"):
    if x["Gender"] == "M":
        x["Gender"] = "male"
    if x["Gender"] == "F":
        x["Gender"] = "female"
    for elem in df2.to_dict(orient="records"):
        if x["CAP"] >= elem["CAP.1"] and x["CAP"] <= elem["CAP.2"]:
            x["Province"] = elem["Provincia"]
            break
    lista.append((x['UserID'],x['Gender'],x['Age'],x['CAP'],x['Province'],x['Work'],))

c = create_db_connection('daitv12')
q = f"""INSERT INTO utenti(UserID,Gender,Age,CAP,Province,Work) VALUES(%s,%s,%s,%s,%s,%s)"""


execute_many_query(c,q,lista)


