"""
1. 가수명의 spotify 정보 조회( 2nd.py )
    - 1st의 csv 파일의 가수명으로 id, 대표곡 조회
    - csv 파일로 저장 후 엑셀로 수기 필터링
"""
# 1st 수집한 csv 파일에서 가수명으로 spotify api로 artist.id 수집 / 대표곡 수집 ( 수기 필터링 용 )
# 유니크하지 않은 이름은 수기로 필터링 해야함
# Spotify API key 준비

import json, time, pprint
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

# client_id , secret 비밀 파일
file_path = './secrets.json'
artist_file_name = 'artists_tmp.csv'

SPO_API_ID = ''
SPO_API_SECRET = ''

with open(file_path, 'r') as file:
    data = json.load(file)
    SPO_API_ID = data['spo_api_id']
    SPO_API_SECRET = data['spo_api_secret']

# spotify api auth
client_credentials_manager = SpotifyClientCredentials(client_id=SPO_API_ID, client_secret=SPO_API_SECRET)
spo = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

artist_csv = pd.read_csv(
    artist_file_name, 
    encoding='UTF-8', 
    header=0,
    index_col=0, 
    dtype={'id':'string', 'track':'string', 'album':'string'}
)
# print(artist_csv)

# artist id 호출
for idx, row in artist_csv.iterrows():
    print('-' * 50)
    print(row['artist'])
    result_info = spo.search(q=row['artist'], limit=5, type='artist')
    for art in result_info['artists']['items']:
        if row['artist'] == art['name']:
            print(art['name'], ',', art['id'])
            artist_csv.at[idx, 'id'] = art['id']
        else:
            print('미일치 :', row['artist'], art['name'])
    time.sleep(1) # 과다 호출 방지 ㅎㅎ
    
print('-' * 50)
print(artist_csv)

for idx, row in artist_csv.iterrows():
    print('-' * 50)
    result_album = spo.artist_albums(artist_id=row['id'], limit=50, album_type='single,album')
    cnt = 0
    for alb in result_album['items']:
        artist_id = alb['artists'][0]['id']
        artist_name = alb['artists'][0]['name']
        album_name = alb['name']
        release_date = alb['release_date']
        release_date_precision = alb['release_date_precision'] # day, year 값으로 날짜 처리
        album_id = alb['id']
        total_track = alb['total_tracks']
        album_type = alb['album_group']
        #images = alb['images'][0]['url']
        if row['id'] == artist_id:
            cnt = cnt + 1
            print(cnt, artist_id, artist_name, album_name, release_date, album_id, total_track, album_type)
        #if cnt == 16:
        #    pprint.pprint(alb)
    time.sleep(2)
    # spo.artist_top_tracks(artist_id=row['id'])

# 결과 저장
# artist_csv.to_csv(artist_file_name)
print('-' * 50)