import pandas as pd
import re

df = pd.read_csv("../create db/Elenco Movies definitivo.csv")



def clean_title(title):
    # Pattern per estrarre il titolo e l'anno
    pattern = r'^(.+?),?\s*(the|an|a|il|el)?\s*\((.*?)\)$'
    match = re.match(pattern, title, re.IGNORECASE)
    if match:
        cleaned_title = match.group(1).strip()
        year = match.group(3).strip()
        return cleaned_title, year
    else:
        return title, None

# Applica la funzione alla colonna del titolo
df['Title'], df['year'] = zip(*df['Title'].map(clean_title))
df['Genres'] = df['Genres'].str.split('|')
df = df.explode('Genres')
df.to_csv("cleaned_movies.csv", index=False)



