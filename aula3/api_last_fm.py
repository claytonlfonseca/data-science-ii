#!/usr/bin/python3.5

import json
import requests

if __name__=="__main__":
    url='http://ws.audioscrobbler.com/2.0/?method=geo.gettopartists&country=spain&api_key=04f10cb164ed5f60dbf4d1f4b8bae05c&format=json'
    data = requests.get(url).text
    data = json.loads(data)
    print (data['topartists']['artist'][0]['name'])