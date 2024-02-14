import pandas as pd

df = pd.read_csv("Elenco Movies definitivo.csv")

newdf = []
for x in df.to_dict(orient="records"):
    spl = x["Title"].rsplit("(")
    anno = spl[1].replace(")"," ")
    titolo = spl[0]
    if len(titolo) == 0:
        titolo = "Phantom of The Opera, The"
    if anno == "not_def":
        anno = "1995"
    x['Title'] = titolo
    x['Year'] = anno
    if "--" in x['Genres']:
        x['Genres'] = x['Genres'].replace("--", "|")
    if "dramma" in x['Genres'].lower() or "dramatic" in x['Genres'].lower():
        x['Genres'] = "Drama"
    newdf.append(x)

res = pd.DataFrame(newdf)

res['Title'] = res['Title'].map(lambda x: statsInvertiti(x))
res['Original Title'] = res['Original Title'].map(lambda x: statsInvertiti(x))
res['Original Title'] = res['Original Title'].map(lambda x: x.replace("a.k.a.", ""))
res.to_csv("New_Elenco_Movies_Pulito.csv", index=False)






print(res['Genres'])

res.to_csv("Elenco_Movies_Pulito.csv", index=False)