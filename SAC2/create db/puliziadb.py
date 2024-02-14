import pandas as pd
import re
def statsInvertiti(titolo):
    tlow = titolo.lower()
    listArt = ['The','A',"Il","Le","La","Der","An", "I"]
    for x in listArt:
        if re.search( fr"\b{x.lower()}\b\s$",tlow, re.IGNORECASE) :
            titolo = f"{x} " + re.sub(fr"\b{x.lower()}\b\s$", "",tlow)
    return titolo.replace(", ", "").rstrip()


if __name__ == '__main__':


    df = pd.read_csv("Elenco Movies definitivo.csv")

    newdf = []
    for x in df.to_dict(orient="records"):
        spl = x["Title"].rsplit("(", maxsplit=1)
        anno = spl[1].replace(")", "")
        titolo = spl[0].split("(")
        if len(titolo) == 2:
            titolo1 = titolo[0]
            titolo2 = titolo[1].replace(")", "")
        else:
            titolo1 = titolo[0]
            titolo2 = ""
        if len(titolo1) == 0:
            titolo1 = "Phantom of The Opera, The"
        if anno == "not_def":
            anno = "1995"
        x['Title'] = titolo1
        x['Original Title'] = titolo2
        x['Year'] = anno
        if "--" in x['Genres']:
            x['Genres'] = x['Genres'].replace("--", "|")
        if "dramma" in x['Genres'].lower() or "dramatic" in x['Genres'].lower():
            x['Genres'] = "Drama"
        if "&#8230;" in x['Original Title']:
            x['Original Title'] = x['Original Title'].replace("&#8230;", " ")
        newdf.append(x)

    res = pd.DataFrame(newdf)

    res['Title'] = res['Title'].map(lambda x: statsInvertiti(x))
    res['Original Title'] = res['Original Title'].map(lambda x: statsInvertiti(x))
    res['Original Title'] = res['Original Title'].map(lambda x: x.replace("a.k.a.", ""))
    res.to_csv("New_Elenco_Movies_Pulito.csv", index=False)






    res.to_csv("New_Elenco_Movies_Pulito.csv", index=False)