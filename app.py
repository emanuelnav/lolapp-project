from flask import Flask, render_template, request
from riotwatcher import LolWatcher, ApiError
from decouple import config


app = Flask(__name__)

# global variables
api_key = config('API_KEY')
watcher = LolWatcher(api_key)

@app.route("/")
def home():
  return render_template("main.html")


@app.route('/summoner')
def summoner():
  me = watcher.summoner.by_name(request.args['region'], request.args['summoner-name'])
  my_ranked_stats = watcher.league.by_summoner(request.args['region'], me['id'])
  return render_template("invocador.html", ranked_stats=my_ranked_stats)