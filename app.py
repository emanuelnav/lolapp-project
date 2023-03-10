from flask import Flask, render_template, request
from decouple import config
from my_api import getSummoner, getAllLeagues
import requests

app = Flask(__name__)

@app.route("/")
def home():
  return render_template("main.html")


@app.route('/summoner')
def summoner():
  summoner_name = getSummoner(request.args['region'], request.args['summoner-name'])
  my_ranked_stats = getAllLeagues(request.args['region'], summoner_name['id']) if summoner_name else []
  print(my_ranked_stats)
  return render_template("invocador.html", ranked_stats=my_ranked_stats)