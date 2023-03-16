from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

date = "2005-10-11"

soup = BeautifulSoup(response.text, 'html.parser')

song_list_raw = soup.select(selector="div ul li ul li h3")
song_list = []
for s in range(99):
    song_list.append(song_list_raw[s].getText().replace('\n', ''))