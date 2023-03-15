from decouple import config
import requests
import json

api_key = config('API_KEY')

def getSummoner(region, username):
  url = f"https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{username}"
  try:
    headers = {"X-Riot-Token": api_key}
    response = requests.get(url, headers=headers)
    response.raise_for_status() # raises an HTTPError if the status code is not 200
    return response.json()
  except requests.exceptions.HTTPError as e:
    print("HTTP Error:", e)
    return []

def getAllLeagues(region, summonerId):
  url = f"https://{region}.api.riotgames.com/lol/league/v4/entries/by-summoner/{summonerId}"
  try:
    headers = {"X-Riot-Token": api_key}
    response = requests.get(url, headers=headers)
    response.raise_for_status() # raises an HTTPError if the status code is not 200
    return response.json()
  except requests.exceptions.HTTPError as e:
    print("HTTP Error:", e)
    return []

def getChampionMasteries(region, summonerId):
  url= f"https://{region}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{summonerId}"
  try:
    headers = {"X-Riot-Token": api_key}
    response = requests.get(url, headers=headers)
    response.raise_for_status() # raises an HTTPError if the status code is not 200
    return response.json()
  except requests.exceptions.HTTPError as e:
    print("HTTP Error:", e)
    return []

def getAllChampionsByName():
  url_json = "http://ddragon.leagueoflegends.com/cdn/13.5.1/data/en_US/champion.json"
  try:
    response = requests.get(url_json)
    response.raise_for_status() # raises an HTTPError if the status code is not 200
    json_data = json.loads(response.content)
    names_dict = {}
    for key in json_data['data']:
      row = json_data['data'][key]
      names_dict[row['key']] = row['name']
    return names_dict
  except requests.exceptions.HTTPError as e:
    print("HTTP Error:", e)
    return {}
  except json.JSONDecodeError as e:
    print("JSON Decode Error:", e)
    return {}