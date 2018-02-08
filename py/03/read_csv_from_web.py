import requests
import csv

planets_data = requests.get("http://localhost:8080/planets.csv").text
planets = planets_data.split('\n')
reader = csv.reader(planets, delimiter=',', quotechar='"')
lines = [line for line in reader][:-1]
for line in lines: print(line)

