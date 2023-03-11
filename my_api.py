from decouple import config
import requests

api_key = config('API_KEY')

def getSummoner(region, username):
    url = f"https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{username}"
    headers = {"X-Riot-Token": api_key}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
      return response.json()
    else:
      return []

def getAllLeagues(region, summonerId):
  url = f"https://{region}.api.riotgames.com/lol/league/v4/entries/by-summoner/{summonerId}"
  headers = {"X-Riot-Token": api_key}
  response = requests.get(url, headers=headers)
  if response.status_code == 200:
    return response.json()
  else:
    return []
  
def getChampionMasteries(region, summonerId):
  url= f"https://{region}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{summonerId}"
  headers = {"X-Riot-Token": api_key}
  response = requests.get(url, headers=headers)
  if response.status_code == 200:
    return response.json()
  else:
    return []

def getChampionName(region, champion_id):
  pass