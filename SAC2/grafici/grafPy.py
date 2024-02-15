import seaborn as sns
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import sys
sys.path.append('create db')
from query import Querys 
import matplotlib.pyplot as plt
import folium
import geopandas


def grafico1():

    q = Querys('sacDB')
    result = q.film_for_year()
    df = pd.DataFrame(result, columns=['COUNT(*)', 'Year'])
    df.rename(columns = {'COUNT(*)':'FilmCount'}, inplace = True)
    sns.set_style("whitegrid")
    sns.lineplot(x='Year', y='FilmCount', data=df)
    plt.show()

def grafico2():
    q = Querys('sacDB')
    result = q.film_for_genre()
    print(result)
    df = pd.DataFrame(result, columns=['Genere', 'COUNT(generirel.FilmID)'])
    df.rename(columns = {'COUNT(generirel.FilmID)':'FilmCount'}, inplace = True)
    sns.set_style("whitegrid")

    sns.barplot(x='Genere', y='FilmCount', data=df)
    plt.xticks(rotation=45)
    plt.show()
#grafico2()    

""" def grafico3(): #TODO mi continua a sfuggi' il senso de sta query
    q = Querys('sacDB')
    result = q.film_age_gender()
    print(result)

    df = pd.DataFrame(result, columns=['Title', 'Age_groups'])
    sns.set_style("whitegrid")

    sns.pointplot(x='Title', y='Age_groups', data=df, markers='o')

    plt.show()
    pass """

def grafico4():
    q = Querys('sacDB')
    result = q.user_for_province()
    df = pd.DataFrame(result, columns=['COUNT(*)', 'Province'])
    df.rename(columns = {'COUNT(*)':'UserCount'}, inplace = True)
    df.dropna(inplace=True)
    gdf = gpd.read_file("./grafici/limits_IT_provinces.geojson", driver='GeoJSON')
    gdf = gdf.merge(df, left_on='prov_name', right_on='Province')
    gdf.plot(column='UserCount', cmap='RdYlGn', legend=True)
    #TODO maybe folium pe fallo piu carino
    plt.show()
    

grafico4()

def grafico5():
    q = Querys('sacDB')
    result = q.user_for_work()
    print(result)
    df = pd.DataFrame(result, columns=['COUNT(*)', 'Work'])
    df.rename(columns = {'COUNT(*)':'UserCount'}, inplace = True)
    #sns.set_style("whitegrid")
    colors = sns.color_palette('pastel')[0:5]
    #sns.pieplot(x='Work', y='UserCount', data=df)
    plt.pie(df['UserCount'],  labels = df['Work'], colors = colors, autopct='%.0f%%')
    plt.legend(bbox_to_anchor=(1.1, 1), loc='upper left')
    plt.show()
    

#grafico5()
