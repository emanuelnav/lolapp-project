from riotwatcher import LolWatcher, ApiError
from decouple import config
import pandas as pd

# golbal variables
api_key = config('API_KEY')
watcher = LolWatcher(api_key)
my_region = 'la2'

me = watcher.summoner.by_name(my_region, 'krosz')
my_ranked_stats = watcher.league.by_summoner(my_region, me['id'])
print(my_ranked_stats)
# print(me)