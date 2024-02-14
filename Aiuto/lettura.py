import pandas as pd
lista_colonne = ["Country","Happiness Score", "Economy (GDP per Capita)", "Health (Life Expectancy)","Trust (Government Corruption)","Generosity"]
df_2015 = pd.read_csv("2015.csv", usecols=lista_colonne)
df_2016 = pd.read_csv("2016.csv", usecols=lista_colonne)
df_2017 = pd.read_csv("2017.csv", usecols=lista_colonne)
df_2018 = pd.read_csv("2018.csv", usecols=lista_colonne)
df_2019 = pd.read_csv("2019.csv",usecols=lista_colonne)


