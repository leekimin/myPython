import eyed3
import requests
import json
import pylast
import os

eyed3.log.setLevel("ERROR")

mp3 = eyed3.load("Hoobastank - The Reason.mp3")

print("*" * 50, 'start')
"""
print("artist :", mp3.tag.artist)
print(mp3.tag.album)
print(mp3.tag.album_artist)
print(mp3.tag.title)
print(mp3.tag.track_num.count)
print(mp3.tag.track_num.total)
print(mp3.tag.id)
"""


"""
전체 태그 정보
https://github.com/JayRizzo/Random_Scripts/blob/master/track_meta_id3.py#L9

reference
https://www.last.fm/api/show/track.getInfo

참고
https://jae04099.tistory.com/entry/2-%EC%9D%8C%EC%95%85-%EA%B2%80%EC%83%89%EC%9A%A9-API-%EC%B0%BE%EC%95%84%EB%B3%B4%EA%B8%B0Lastfm-api

"""



def send_api(path, method):
    API_HOST = "https://ws.audioscrobbler.com/2.0/?"
    url = API_HOST + path
    headers = {'Content-Type': 'application/json', 'charset': 'UTF-8', 'Accept': '*/*'}
    body = {
        "key1": "value1"
    }
    
    try:
        if method == 'GET':
            response = requests.get(url, headers=headers)
        elif method == 'POST':
            response = requests.post(url, headers=headers, data=json.dumps(body, ensure_ascii=False, indent="\t"))
        #print("response status %r" % response.status_code)
        #print("response text %r" % response.text)
        return json.loads(response.text)
    except Exception as ex:
        print(ex)




# https://github.com/pylast/pylast
"""
j = send_api('method=album.getinfo&api_key=abcd&artist=Blur&album=Blur&format=json', 'GET')
jf = json.dumps(j['album']['tracks'], indent=4)
print(type(j['album']['tracks']))
"""

import inspect

""" json 읽어서 호출
file_path = './secrets.json'

API_KEY = ''
API_SECRET = ''
API_USERNAME = ''
API_PWD = ''

with open(file_path, 'r') as file:
    data = json.load(file)
    API_KEY = data['apikey']
    API_SECRET = data['apisecret']
    API_USERNAME = data['username']
    API_PWD = data['pwd']

network = pylast.LastFMNetwork(
    api_key=API_KEY,
    api_secret=API_SECRET,
    username=API_USERNAME,
    password_hash=pylast.md5(API_PWD)
)
"""
# 디렉토리 가수명 + 파일곡명으로 조회

# Album Name
# Track Name
# Track Number
# Track Total Number
# 발매일자

"""
track = network.get_track("Oasis", "Don't look back in anger")
track = network.get_track('Hoobastank', 'The Reason')
print(vars(track))

album = network.get_album('Oasis', 'Stop the Clocks')
album = network.get_album('Hoobastank', 'The Reason')

# print(album.get_tracks())
print(len(album.get_tracks()))

for t in album.get_tracks():
    print(vars(t))
"""

"""
with os.scandir(rootdir) as entries:
    for entry in entries:
#        if entry.is_dir() and entry.name.startswith('00'):
#            print(entry.name)
        print(entry.name)
"""
from pathlib import Path

rootdir = r'D:\_my\sample'
#rootdir = r'D:\_my\1105_conf'

class Music:
    def __init__(self, artist, track) -> None:
        self.artist = artist
        self.track = track

    def debug(self):
        print('* artist : ', self.artist)
        print('* track : ', self.track)

arrList = list()
arrAllList = list()

def listdirs(rootdir):
    for it in os.scandir(rootdir):
        if it.is_dir():
            listdirs(it)
        if it.is_file() and (it.name.find('.mp3') > -1 or it.name.find('.flac') > -1):
            p = Path(it.path)
            m = Music(p.parent.name, it.name)
            arrList.append(m)
        if it.is_file() and (it.name.find('.mp3') > -1 or it.name.find('.flac') > -1):
            arrAllList.append(it.name)

listdirs(rootdir)
print(len(arrAllList))
print(arrAllList[0])


print("*" * 50, 'end')


file_path = './secrets.json'

SPO_API_ID = ''
SPO_API_SECRET = ''

with open(file_path, 'r') as file:
    data = json.load(file)
    SPO_API_ID = data['spo_api_id']
    SPO_API_SECRET = data['spo_api_secret']

"""
def send_spotify_api(path, method):
    #API_HOST = "https://ws.audioscrobbler.com/2.0/?"
    url = path
    headers = {'Content-Type': 'application/json', 'charset': 'UTF-8', 'Accept': '*/*', 'Authorization': 'Bearer ' + SPO_API_SECRET}
    body = {
        "key1": "value1"
    }
    
    try:
        if method == 'GET':
            response = requests.get(url, headers=headers)
        elif method == 'POST':
            response = requests.post(url, headers=headers, data=json.dumps(body, ensure_ascii=False, indent="\t"))
        #print("response status %r" % response.status_code)
        #print("response text %r" % response.text)
        return json.loads(response.text)
    except Exception as ex:
        print(ex)


res = send_spotify_api('https://api.spotify.com/v1/search?q=The+Reason&type=track', 'GET')
print(res)
"""
import pprint
"""
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

cid = SPO_API_ID
secret = SPO_API_SECRET

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

result = sp.search("Song 2", limit=1, type="track")
pprint.pprint(result)
"""





# https://developer.spotify.com/documentation/web-api/reference/search




"""
ddd = {
	"tracks": {
		"href": "https://api.spotify.com/v1/search?query=Song+2&type=track&offset=0&limit=1",
		"items": [
			{
				"album": {
					"album_type": "album",
					"artists": [
						{
							"external_urls": {
								"spotify": "https://open.spotify.com/artist/7MhMgCo0Bl0Kukl93PZbYS"
							},
							"href": "https://api.spotify.com/v1/artists/7MhMgCo0Bl0Kukl93PZbYS",
							"id": "7MhMgCo0Bl0Kukl93PZbYS",
							"name": "Blur",
							"type": "artist",
							"uri": "spotify:artist:7MhMgCo0Bl0Kukl93PZbYS"
						}
					],
					"available_markets": [
						"AR",
						"XK","XK","XK","XK"
					],
					"external_urls": {
						"spotify": "https://open.spotify.com/album/7HvIrSkKGJCzd8AKyjTJ6Q"
					},
					"href": "https://api.spotify.com/v1/albums/7HvIrSkKGJCzd8AKyjTJ6Q",
					"id": "7HvIrSkKGJCzd8AKyjTJ6Q",
					"images": [
						{
							"height": 640,
							"url": "https://i.scdn.co/image/ab67616d0000b273de114203356c1f7b136960b6",
							"width": 640
						},
						{
							"height": 300,
							"url": "https://i.scdn.co/image/ab67616d00001e02de114203356c1f7b136960b6",
							"width": 300
						},
						{
							"height": 64,
							"url": "https://i.scdn.co/image/ab67616d00004851de114203356c1f7b136960b6",
							"width": 64
						}
					],
					"name": "Blur (Special Edition)",
					"release_date": "1997-02-10",
					"release_date_precision": "day",
					"total_tracks": 32,
					"type": "album",
					"uri": "spotify:album:7HvIrSkKGJCzd8AKyjTJ6Q"
				},
				"artists": [
					{
						"external_urls": {
							"spotify": "https://open.spotify.com/artist/7MhMgCo0Bl0Kukl93PZbYS"
						},
						"href": "https://api.spotify.com/v1/artists/7MhMgCo0Bl0Kukl93PZbYS",
						"id": "7MhMgCo0Bl0Kukl93PZbYS",
						"name": "Blur",
						"type": "artist",
						"uri": "spotify:artist:7MhMgCo0Bl0Kukl93PZbYS"
					}
				],
				"available_markets": [
					"AR",
					"XK"
				],
				"disc_number": 1,
				"duration_ms": 121160,
				"explicit": "False",
				"external_ids": {
					"isrc": "GBAYE1200348"
				},
				"external_urls": {
					"spotify": "https://open.spotify.com/track/1FTSo4v6BOZH9QxKc3MbVM"
				},
				"href": "https://api.spotify.com/v1/tracks/1FTSo4v6BOZH9QxKc3MbVM",
				"id": "1FTSo4v6BOZH9QxKc3MbVM",
				"is_local": "False",
				"name": "Song 2 - 2012 Remaster",
				"popularity": 82,
				"preview_url": "https://p.scdn.co/mp3-preview/2c2b4ad08b6ef072182e9b38c386f54623aef4fc?cid=6a41ee82e4a64ae9b42399684d8e25d6",
				"track_number": 2,
				"type": "track",
				"uri": "spotify:track:1FTSo4v6BOZH9QxKc3MbVM"
			}
		],
		"limit": 1,
		"next": "https://api.spotify.com/v1/search?query=Song+2&type=track&offset=1&limit=1",
		"offset": 0,
		"previous": "None",
		"total": 617
	}
}
"""
# obj2 = json.loads(ddd)

# pprint.pprint(len(ddd['tracks']['items'][0]['album']['available_markets']))
"""
markets = ddd['tracks']['items'][0]['album']['available_markets']

for key, val in ddd.items():
    print(key)
"""
#ttt = Tracks(**ddd)

#print(ttt)
