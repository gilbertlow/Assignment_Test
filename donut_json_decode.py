
from configparser import InterpolationSyntaxError
import pandas as pd
import json
from pandas import DataFrame
from pandas.io.json import json_normalize

with open('D:/ELK/ACE Digital/Sample.json') as f:
    lines  = json.load(f)
  
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)

lines1  = pd.DataFrame.from_dict(lines)
#data1 = pd.DataFrame.from_dict(lines)
#data2 = pd.json_normalize(data1, max_level=4)
#print(data2)

# dynamicly read the list of json item for 0, 1 etc
item0topping= pd.json_normalize(lines["items"]["item"][0], record_path='topping', meta=['id','name', 'ppu', 'type'], record_prefix='topping_')
print(item0topping)


# dynamicly read the batter list of json item for 0, 1 etc
batter0 = pd.json_normalize(lines["items"]["item"][0]['batters'], record_path='batter')
print(batter0)

# concat & loop batter to topping and form the json 

# write to file in json_normalize format
