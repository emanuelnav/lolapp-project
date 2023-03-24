import pandas as pd
from my_api import *
# import matplotlib
# matplotlib.use('Agg')
import os
import matplotlib.pyplot as plt
plt.switch_backend('agg')

def getMasteriesChampionsGraph(region, summonerId):
    champion_masteries = get_champion_masteries(region, summonerId)
    all_champs_name = get_all_champions_by_name()

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



    df = pd.DataFrame(champion_masteries)
    #print(df.head())

    x_values = df['championId'].head()
    y_values = df['championPoints'].head()

    champion_level = y_values.values.tolist()
    champion_ids = x_values.values.tolist()
    champion_ids_str = [str(x) for x in champion_ids]

    champion_names = []
    for i in champion_ids_str:
        champion_names.append(all_champs_name[i])
    print(champion_names)



    ### GRAFICOS 

    plt.bar(champion_names, champion_level, width=0.5, color=['#5c58b6','#b457ce','#5994ce','#3a4e93'])
    plt.title('Maestria de campeon mas alta')
    plt.xlabel('Campeones')
    plt.ylabel('Puntos')
    plt.style.use('seaborn-darkgrid')
    #plt.show()
    plt.savefig(os.path.join('static', 'images', 'graph.png'))
    return plt
# summoner_name = get_summoner('la2','krosz')
# getMasteriesChampionsGraph('la2',summoner_name['id'])
