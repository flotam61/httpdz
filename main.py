from pprint import pprint

import requests

hero = {"Hulk": "https://superheroapi.com/api/2619421814940190/search/Hulk",
        "Captain_America": "https://superheroapi.com/api/2619421814940190/search/Captain_America",
        "Thanos": "https://superheroapi.com/api/2619421814940190/search/Thanos"}

heroid = {}
heroint = {}

def find_hero_id():
    for k in hero.items():
        url = k[1]
        response = requests.get(url, timeout=5)
        x = response.json()["results"]
        y = x[0]
        r = y["id"]
        heroid[k[0]] = r


def find_hero_int():
    for y in heroid.items():
        id = y[1]
        url = "https://superheroapi.com/api/2619421814940190/" + id
        response = requests.get(url, timeout=5)
        x = response.json()["powerstats"]
        u = int(x["intelligence"])
        heroint[y[0]] = u



find_hero_id()
find_hero_int()

best_hero = max(heroint, key=heroint.get)

print("Самый умный персонаж", best_hero)

