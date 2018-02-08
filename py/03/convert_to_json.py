import json
from get_planet_data import get_planet_data
planets=get_planet_data()
print(json.dumps(planets, indent=4))