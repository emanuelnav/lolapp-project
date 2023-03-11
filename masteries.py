import pandas as pd 
from my_api import *
import requests
import matplotlib.pyplot as plt
import numpy as np
import json

summoner_name = getSummoner('la2', 'anitsoga')
champion_masteries = getChampionMasteries('la2', summoner_name['id'])
url_json = "http://ddragon.leagueoflegends.com/cdn/13.5.1/data/en_US/champion.json"
response = requests.get(url_json)
if response.status_code == 200:
   data = json.loads(response.content)
   champ_dict = data['data']
else:
    print("Error en los datos")

names_dict = {}
for key in champ_dict:
    row = champ_dict[key]
    names_dict[row['key']] = row['name']



df = pd.DataFrame(champion_masteries)
#print(df.head())

x_values = df['championId'].head()
y_values = df['championLevel']

champion_ids = x_values.values.tolist()
champion_ids_str = [str(x) for x in champion_ids]

champion_names = []
for i in champion_ids_str:
    champion_names.append(names_dict[i])
print(champion_names)






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
