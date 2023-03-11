import pandas as pd
from my_api import *
import requests
import matplotlib.pyplot as plt
import numpy as np

def getMasteriesChampionsGraph(region, summonerId):
    champion_masteries = getChampionMasteries(region, summonerId)
    all_champs_name = getAllChampionsByName()

    df = pd.DataFrame(champion_masteries)
    #print(df.head())

    x_values = df['championId'].head()
    y_values = df['championLevel']

    champion_ids = x_values.values.tolist()
    champion_ids_str = [str(x) for x in champion_ids]

    champion_names = []
    for i in champion_ids_str:
        champion_names.append(all_champs_name[i])

    # plt.hist(x_values)
    # plt.title('Champions points')
    # ax = plt.subplot()
    # ax.set_xticks(x_values)
    # plt.show()


    # plt.bar(x_values, y_values)          #El gráfico
    # plt.title('Champion y nivel')        #El título
    # ax = plt.subplot()                   #Axis
    # ax.set_xticks(x_values)              #Eje x
    # ax.set_xticklabels(x_values)         #Etiquetas del eje x
    # ax.set_xlabel('Campeon')             #Nombre del eje x
    # ax.set_ylabel('level')               #Nombre del eje y
    # plt.show()
    return champion_names