from flask import Flask, render_template, request
from decouple import config
import requests

app = Flask(__name__)

# Global Variables
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

@app.route("/")
def home():
  return render_template("main.html")


@app.route('/summoner')
def summoner():
  summoner_name = getSummoner(request.args['region'], request.args['summoner-name'])
  my_ranked_stats = getAllLeagues(request.args['region'], summoner_name['id']) if summoner_name else []
  print(my_ranked_stats)
  return render_template("invocador.html", ranked_stats=my_ranked_stats)