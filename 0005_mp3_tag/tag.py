import eyed3
import requests
import json
import pylast
import os
import pprint
from pathlib import Path
from func import get_spotify_search, track_info
import pandas as pd

print("*" * 50, 'start')

rootdir = r'D:\_my\sample'

"""
secrets.json
{
    "spo_api_id": "key",
    "spo_api_secret": "key"
}
"""
# 루트 경로 하위의 파일 리스트 조회

class Music:
    artist : str # 상위 폴더명이라 아티스트 또는 앨범명
    track : str 
    full_path : str

    def __init__(self, artist, track, full_path) -> None:
        self.artist = artist
        self.track = track
        self.full_path = full_path

    def debug(self):
        print('*' * 40, 'debug')
        print('* artist : ', self.artist)
        print('* track : ', self.track)
        print('* full_path : ', self.full_path)

arrList = list()

def listdirs(rootdir):
    for it in os.scandir(rootdir):
        if it.is_dir():
            listdirs(it)
        if it.is_file() and (it.name.find('.mp3') > -1 or it.name.find('.flac') > -1):
            p = Path(it.path)
            n, e = os.path.splitext(it.name)
            m = Music(p.parent.name, n, it.path)
            arrList.append(m)

listdirs(rootdir)

# Spotify API key 준비
file_path = './secrets.json'

SPO_API_ID = ''
SPO_API_SECRET = ''

with open(file_path, 'r') as file:
    data = json.load(file)
    SPO_API_ID = data['spo_api_id']
    SPO_API_SECRET = data['spo_api_secret']

# 조회한 파일명으로 API 검색
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials(client_id=SPO_API_ID, client_secret=SPO_API_SECRET)
spo = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

eyed3.log.setLevel("ERROR")

"""
import eyed3

audio_file = eyed3.load("test.mp3")
album_name = audio_file.tag.album
artist_name = audio_file.tag.artist
for image in audio_file.tag.images:
    image_file = open("{0} - {1}({2}).jpg".format(artist_name, album_name, image.picture_type), "wb")
    print("Writing image file: {0} - {1}({2}).jpg".format(artist_name, album_name, image.picture_type))
    image_file.write(image.image_data)
    image_file.close()
"""

# 파일의 tag 정보 읽고 API 정보와 비교
for mp3 in arrList:
    #print(eyed3.id3.ID3_V2_2)
    #print(mp3.debug())
    #track_info(mp3.full_path)
    mp3_tmp = eyed3.load(mp3.full_path)
    for img in mp3_tmp.tag.images:
        print(img)

    # image delete
    #mp3_tmp.tag.images.remove(u'')

    # image add from file
    #img_tmp = open('cover.png', 'rb')
    #mp3_tmp.tag.images.set(3, img_tmp.read(), 'image/png', u'')
    mp3_tmp.tag.save()

    # UNSYNCEDLYRICS
    
    #print(mp3_tmp.tag.album, mp3_tmp.tag.getBestDate(), mp3_tmp.tag.title)
    #print(mp3_tmp.tag.header.version)
    #print(mp3_tmp.tag.isV1())
    #print(mp3_tmp.tag.isV2())
    #print(mp3_tmp.tag.header.major_version)
    #print(mp3_tmp.tag.header.minor_version)
    #print(mp3_tmp.tag.header.rev_version)
    """
    res = spo.search(mp3.track + ' year:2003', limit=1, type="track")

    cnt = 0
    
    for item in res['tracks']['items']:
        cnt = cnt + 1
        
        print('*' * 50, 'item data', cnt)
        
        artist_name = item['album']['artists'][0]['name'] 
        album_name = item['album']['name']
        release_date = item['album']['release_date']

        disc_num = item['disc_number']
        track_name = item['name']
        track_num = item['track_number']

        print("*" * 50, 'search...')
        print("* artist_name :", artist_name)
        print("* album_name :", album_name)
        print("* release_date :", release_date)
        print("* disc_num :", disc_num)
        print("* track_name :", track_name)
        print("* track_num :", track_num)
    """

#df = pd.DataFrame([{"a":"123"},{"a":"444"}])
#print(df)
#print(df.index[1])

print("*" * 50, 'end')





# tag 수정 후 저장