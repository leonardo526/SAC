import seaborn as sns
import sys
sys.path.append('create db')
from query import Querys 


def grafico1():

    q = Querys('sacDB')
    result = q.film_for_year()
    print(result)
    #tips = sns.load_dataset("tips")

grafico1()