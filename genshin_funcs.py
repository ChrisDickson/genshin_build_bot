from cmath import e
from lxml import html
import requests
from datetime import datetime
import discord
import json

url = "https://keqingmains.com/infographics/"
page = requests.get(url)
tree = html.fromstring(page.content)

def get_build(character):
    '''
    Take in a character name, return the KQM card for it - if multiple return all
    '''
    out_message = []
    cards = tree.xpath(f"//img[contains(translate(@alt, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'),'{character}')]")
    if len(cards) == 0:
        out_message.append(f"Could not find card for character {character}")
    else:
        for c in cards:
            out_message.append(c.get('src'))
    
    return out_message

f = open("sets.json")
set_data = json.load(f)
def get_set(set_abb):
    out_message = []
    set = set_data[set_abb][0]
    out_message.append(f'{set["name"]} \n{set["2set"]} \n{set["4set"]} \n{set["loc"]}')
    return out_message
