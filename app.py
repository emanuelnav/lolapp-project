from flask import Flask, render_template
from riotwatcher import LolWatcher, ApiError
from decouple import config

app = Flask(__name__)

# golbal variables
api_key = config('API_KEY')
watcher = LolWatcher(api_key)
my_region = 'la2'

me = watcher.summoner.by_name(my_region, 'krosz')
my_ranked_stats = watcher.league.by_summoner(my_region, me['id'])

@app.route("/")
def home():
  return render_template("main.html", ranked_stats=my_ranked_stats)