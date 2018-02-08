import pandas as pd
from get_planet_data import get_planet_data

# construct a data from from the list
planets = get_planet_data()
planets_df = pd.DataFrame(planets).set_index('Name')
planets_df.to_csv("../../www/planets_pandas.csv")
