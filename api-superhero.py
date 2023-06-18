import requests
from pprint import pprint
import json

url = "https://akabab.github.io/superhero-api/api"
response = requests.get(f"{url}/all.json")

def list_heroes(text):
    list = text.strip("[]").split("\n  },")
    for id, hero in enumerate(list):
        if id < (len(list) - 1):
            list[id] = hero + "\n  }"
    return list


def id_hero(names, all_heroes):
    id_heroes = {}
    for name in names:
        for hero in all_heroes:
            i = json.loads(hero)
            if i["name"] == name:
                id_heroes[i["name"]] = i["id"]
    return id_heroes

def intelligence_heroes(heroes):
    url = "https://akabab.github.io/superhero-api/api"
    intelligence_heroes = []
    for name, id in heroes.items():
        response = requests.get(f"{url}/powerstats/{id}.json")
        intelligence = json.loads(response.text)["intelligence"]
        intelligence_heroes.append((name, id, intelligence))
    return intelligence_heroes



names = ["Hulk", "Captain America", "Thanos"]
intelligence = intelligence_heroes(id_hero(names, list_heroes(response.text)))
intelligence.sort(key=lambda a: a[2], reverse=True)
print(f"Самый умный супергерой: {intelligence[0][0]}")
