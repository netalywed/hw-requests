import requests
import operator

def get_intellegence(name):
    response = requests.get("https://superheroapi.com/api/2619421814940190/search/" + name)
    r = response.json()
    Hero_id = r["results"][0]["id"]

    response_app = requests.get("https://superheroapi.com/api/2619421814940190/" + Hero_id + "/powerstats")
    r_app = response_app.json()
    Hero_int = r_app['intelligence']
    return Hero_int

def define_th_hero(heros_list):
    heros_dict = {}
    for hero in heros_list:
        hero_intel = get_intellegence(hero)
        heros_dict[hero] = int(hero_intel)
    heros_dict = sorted(heros_dict.items(), key=operator.itemgetter(1))
    the_hero = heros_dict[-1][0]
    return the_hero


h_list = ["Hulk", "Captain America", "Thanos"]
my_hero = define_th_hero(h_list)
print(my_hero)


