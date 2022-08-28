# create a script that will download videos from ted.com
# and save them to this directory

import requests

from bs4 import BeautifulSoup

import sys  # this is for argument parsing

import json  # this is for json processing

url = 'https://www.ted.com/talks/alicia_chong_rodriguez_a_smart_bra_for_better_heart_health'

r = requests.get(url)
print("Downloading video...")

soup = BeautifulSoup(r.content, "html.parser")

next_data_script = soup.find(id="__NEXT_DATA__")

data_json = next_data_script.string

player_data = json.loads(data_json)['props']['pageProps']['videoData']['playerData']

url_content = json.loads(player_data)['resources']['h264'][0]['file']

mp4_response = requests.get(url_content)

file_name = 'ted_talk_video.mp4'

with open(file_name, 'wb') as f:
    f.write(mp4_response.content)

print("Download complete")