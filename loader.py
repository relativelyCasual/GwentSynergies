import urllib
import requests
import json

url = 'https://api.gwentapi.com/v0'

#response = requests.get(url)

#content = response.content.decode("utf8")

#js = json.loads(content)

#urlcards = js['cards']

#print(urlcards)

def get_url(URL):
    response = requests.get(URL)
    content = response.content.decode("utf8")

    return content

def get_json(URL):
    content = get_url(URL)
    js = json.loads(content)
    return js

urlCards = get_json(url)['cards']
#print(urlCards)
cardPage = get_url(urlCards)

print(cardPage["results"])
#print(get_json(urlCards))

print

