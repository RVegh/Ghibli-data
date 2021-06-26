import pandas as pd
import requests

url = 'https://ghibliapi.herokuapp.com/films'

r = requests.get(url)
json = r.json()

films = pd.DataFrame(json).head()

print(films)

