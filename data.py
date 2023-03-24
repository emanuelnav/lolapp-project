import pandas as pd
import numpy as np
from datetime import date, timedelta
from my_api import *

champion_masteries = get_champion_masteries(region, summonerId)
df = df = pd.DataFrame(champion_masteries)
print(df.head())
