import eyed3
import requests
import json
import pylast
import os
import pprint
from pathlib import Path
from func import get_spotify_search, track_info
import pandas as pd

print("*" * 70, 'start')

# 음원파일 루트 경로
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

arrFileList = list()
arrFolderList = list()

def listdirs(rootdir):
    for it in os.scandir(rootdir):
        if it.is_dir():
            listdirs(it)
            d = Music(it.name, 0, it.path)
            arrFolderList.append(d)
        if it.is_file() and (it.name.find('.mp3') > -1 or it.name.find('.flac') > -1):
            p = Path(it.path)
            n, e = os.path.splitext(it.name)
            m = Music(p.parent.name, n, it.path)
            arrFileList.append(m)

listdirs(rootdir)

# 가수명만 뽑자. 디렉토리 구조는 개인 취향이라 가수명이 존재하는 폴더 레벨로 일괄 수집
for f in arrFolderList:
    depth = len(f.full_path.split('\\'))
    name = f.artist
    if depth == 4:
        print(f"Depth : {depth}, {name}")
exit()

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
eyed3 documentation
https://eyed3.readthedocs.io/en/latest/
"""

import pandas as pd
from pandas import DataFrame

tempcsv = pd.read_csv('temp.csv', encoding='UTF-8', header=None, index_col=None)
#pprint.pprint(tempcsv)
for idx, row in tempcsv.iterrows():
    print('=' * 10)
    print(idx, row)


#dtFrame2 = DataFrame(tempcsv)
#dtFrame2.to_csv('temp.csv', encoding='UTF-8', header=None, index=None)
exit()

# artists 검색
resArtists = spo.search(q="Zone", limit=3, type="artist")
for art in resArtists['artists']['items']:
    print(art['name'], ',', art['id'])
exit()

"""
read_csv = pd.read_csv('artists.csv', encoding="UTF-8")
print(len(read_csv))
exit()
"""

resAlbums = spo.artist_albums(artist_id='4H1S8RTYv4vN3SiM5uSZSa', limit=30, offset=0, album_type='album')
#pprint.pprint(resAlbums)
#exit()
dicAlbum = []

cnts = 0
for alb in resAlbums['items']:
    cnts = cnts + 1
    #print('반복...', cnts)
    #print(cnts, alb['name'], alb['release_date'], alb['id'], alb['total_tracks'], alb['type'])
    #dicAlbum.append(alb['name'], alb['release_date'], alb['id'], alb['total_tracks'], alb['type'])
    dicAlbum.append(
        dict(
            #artist_id=alb['artists'][0]['id'],
            artist_name=alb['artists'][0]['name'],
            name=alb['name'], 
            release_date=alb['release_date'],
            id=alb['id'],
            total_tracks=alb['total_tracks'],
            type=alb['type'],
            #images=alb['images'][0]['url'],
        )
    )
    
dtFrame = DataFrame(dicAlbum)
print(dtFrame)
# print(len(dtFrame))
# dtFrame.to_html('test.html')
#dtFrame.to_csv('test.csv', encoding="UTF-8")

from mutagen.id3 import USLT, ID3

# 파일의 tag 정보 읽고 API 정보와 비교
for mp3 in arrList:
    #print(eyed3.id3.ID3_V2_2)
    #print(mp3.debug())
    #track_info(mp3.full_path)

    # 앨범 커버 등록 ( file open or url open)
    """
    mp3_tmp = eyed3.load(mp3.full_path)
    for img in mp3_tmp.tag.images:
        print(img)

    # image delete
    #mp3_tmp.tag.images.remove(u'')

    # image add from file
    #img_tmp = open('cover.png', 'rb')
    #mp3_tmp.tag.images.set(3, img_tmp.read(), 'image/png', u'')
    #mp3_tmp.tag.images.set(3, '', '', u'', 'http://localhost:8800/test.png')
    #mp3_tmp.tag.save()
    """
    # 가사 등록 / 제거 - 가사 API 연동까지하면 Good! ( UNSYNCEDLYRICS )
    """
    mp3_lyrics = ID3(mp3.full_path)

    #mp3_lyrics.add(USLT(text='gasa in for custom333', lang='eng'))
    #mp3_lyrics.add(USLT(text='gasa in for custom333'))
    #mp3_lyrics.setall('USLT::XXX', '')
    #mp3_lyrics.save()
    
    pprint.pprint(mp3_lyrics)
    #pprint.pprint(mp3_lyrics['USLT::XXX'])
    #pprint.pprint(mp3_lyrics['USLT::eng'])

    # https://eyed3.readthedocs.io/en/latest/_modules/eyed3/id3/frames.html
    # b"ULT": b"USLT",  # UNSYNCEDLYRICS unsynchronised lyrics/text transcription
    # b"STC": b"SYTC",  # SYNCEDTEMPO synchronised tempo codes
    # b"SLT": b"SYLT",  # SYNCEDLYRICS synchronised lyrics/text

    if "USLT::XXX" in mp3_lyrics:
        print('USLT::XXX is exist =>', mp3_lyrics['USLT::XXX'])
    else:
        print('not exist')
    """

    #print(mp3_tmp.tag.album, mp3_tmp.tag.getBestDate(), mp3_tmp.tag.title)
    #print(mp3_tmp.tag.header.version)
    #print(mp3_tmp.tag.isV1())
    #print(mp3_tmp.tag.isV2())
    #print(mp3_tmp.tag.header.major_version)
    #print(mp3_tmp.tag.header.minor_version)
    #print(mp3_tmp.tag.header.rev_version)
    
    """
    res = spo.search(mp3.track, limit=50, type="track")

    cnt = 0
    
    for item in res['tracks']['items']:
        artist_name = item['album']['artists'][0]['name'] 
        album_name = item['album']['name']
        release_date = item['album']['release_date']

        disc_num = item['disc_number']
        track_name = item['name']
        track_num = item['track_number']

        if artist_name == 'Hoobastank':
            cnt = cnt + 1
            print('*' * 50, 'item data', cnt)
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

print("*" * 70, 'end')





# tag 수정 후 저장