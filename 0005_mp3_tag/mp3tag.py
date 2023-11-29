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



data = {"name":"123", "username":"my"}

class User(object):
    def __init__(self, name, username):
        self.name = name
        self.username = username

import json
#j = json.loads(data)
u = User(**data)

print(vars(u))

# https://developer.spotify.com/documentation/web-api/reference/search

##################### def
from typing import List
from typing import Any
from dataclasses import dataclass
import json

@dataclass
class Image:
    height: int
    url: str
    width: int

    @staticmethod
    def from_dict(obj: Any) -> 'Image':
        _height = int(obj.get("height"))
        _url = str(obj.get("url"))
        _width = int(obj.get("width"))
        return Image(_height, _url, _width)

@dataclass
class ExternalUrls:
    spotify: str

    @staticmethod
    def from_dict(obj: Any) -> 'ExternalUrls':
        _spotify = str(obj.get("spotify"))
        return ExternalUrls(_spotify)

@dataclass
class Artist:
    external_urls: ExternalUrls
    href: str
    id: str
    name: str
    type: str
    uri: str

    @staticmethod
    def from_dict(obj: Any) -> 'Artist':
        _external_urls = ExternalUrls.from_dict(obj.get("external_urls"))
        _href = str(obj.get("href"))
        _id = str(obj.get("id"))
        _name = str(obj.get("name"))
        _type = str(obj.get("type"))
        _uri = str(obj.get("uri"))
        return Artist(_external_urls, _href, _id, _name, _type, _uri)

@dataclass
class Album:
    album_type: str
    artists: List[Artist]
    available_markets: List[str]
    external_urls: ExternalUrls
    href: str
    id: str
    images: List[Image]
    name: str
    release_date: str
    release_date_precision: str
    total_tracks: int
    type: str
    uri: str

    @staticmethod
    def from_dict(obj: Any) -> 'Album':
        _album_type = str(obj.get("album_type"))
        _artists = [Artist.from_dict(y) for y in obj.get("artists")]
        _available_markets = [Artist.from_dict(y) for y in obj.get("available_markets")]
        _external_urls = ExternalUrls.from_dict(obj.get("external_urls"))
        _href = str(obj.get("href"))
        _id = str(obj.get("id"))
        _images = [Image.from_dict(y) for y in obj.get("images")]
        _name = str(obj.get("name"))
        _release_date = str(obj.get("release_date"))
        _release_date_precision = str(obj.get("release_date_precision"))
        _total_tracks = int(obj.get("total_tracks"))
        _type = str(obj.get("type"))
        _uri = str(obj.get("uri"))
        return Album(_album_type, _artists, _available_markets, _external_urls, _href, _id, _images, _name, _release_date, _release_date_precision, _total_tracks, _type, _uri)

@dataclass
class ExternalIds:
    isrc: str

    @staticmethod
    def from_dict(obj: Any) -> 'ExternalIds':
        _isrc = str(obj.get("isrc"))
        return ExternalIds(_isrc)


@dataclass
class Item:
    album: Album
    artists: List[Artist]
    available_markets: List[str]
    disc_number: int
    duration_ms: int
    explicit: str
    external_ids: ExternalIds
    external_urls: ExternalUrls
    href: str
    id: str
    is_local: str
    name: str
    popularity: int
    preview_url: str
    track_number: int
    type: str
    uri: str

    @staticmethod
    def from_dict(obj: Any) -> 'Item':
        _album = Album.from_dict(obj.get("album"))
        _artists = [Artist.from_dict(y) for y in obj.get("artists")]
        _available_markets = [Artist.from_dict(y) for y in obj.get("available_markets")]
        _disc_number = int(obj.get("disc_number"))
        _duration_ms = int(obj.get("duration_ms"))
        _explicit = str(obj.get("explicit"))
        _external_ids = ExternalIds.from_dict(obj.get("external_ids"))
        _external_urls = ExternalUrls.from_dict(obj.get("external_urls"))
        _href = str(obj.get("href"))
        _id = str(obj.get("id"))
        _is_local = str(obj.get("is_local"))
        _name = str(obj.get("name"))
        _popularity = int(obj.get("popularity"))
        _preview_url = str(obj.get("preview_url"))
        _track_number = int(obj.get("track_number"))
        _type = str(obj.get("type"))
        _uri = str(obj.get("uri"))
        return Item(_album, _artists, _available_markets, _disc_number, _duration_ms, _explicit, _external_ids, _external_urls, _href, _id, _is_local, _name, _popularity, _preview_url, _track_number, _type, _uri)

@dataclass
class Tracks:
    href: str
    items: List[Item]
    limit: int
    next: str
    offset: int
    previous: str
    total: int

    @staticmethod
    def from_dict(obj: Any) -> 'Tracks':
        _href = str(obj.get("href"))
        _items = [Item.from_dict(y) for y in obj.get("items")]
        _limit = int(obj.get("limit"))
        _next = str(obj.get("next"))
        _offset = int(obj.get("offset"))
        _previous = str(obj.get("previous"))
        _total = int(obj.get("total"))
        return Tracks(_href, _items, _limit, _next, _offset, _previous, _total)

@dataclass
class Root:
    tracks: Tracks

    @staticmethod
    def from_dict(obj: Any) -> 'Root':
        _tracks = Tracks.from_dict(obj.get("tracks"))
        return Root(_tracks)



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
						"XK"
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


ttt = Tracks(**ddd)

print(ttt)
pprint.pprint('test')