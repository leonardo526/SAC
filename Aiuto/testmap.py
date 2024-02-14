import pandas as pd

statistic_df = pd.read_csv(
    "2015.csv",
    encoding='latin-1',
    header=0,
    usecols=["Country","Happiness Score"]
)
print(statistic_df)
""" statistic_df.rename(
    columns = {
        statistic_df.columns[0]: 'Region or Country', 
        'Value': 'Urban Percentage'
    }, 
    inplace=True
) """

import geopandas

country_geopandas = geopandas.read_file(
    geopandas.datasets.get_path('naturalearth_lowres')
)
country_geopandas = country_geopandas.merge(
    statistic_df, # this should be the pandas with statistics at country level
    how='inner', 
    left_on=['name'], 
    right_on=['Country']
)

print(country_geopandas)

from datetime import datetime
import folium


urban_area_map = folium.Map()
folium.Choropleth(
    geo_data=country_geopandas,
    name='choropleth',
    data=statistic_df,
    columns=['Country', 'Happiness Score'],
    key_on='feature.properties.name',
    fill_color='Greens',
    nan_fill_color='Grey',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Percentage of population living in Urban areas'
).add_to(urban_area_map)
urban_area_map.save(f'./funzionapls.html')