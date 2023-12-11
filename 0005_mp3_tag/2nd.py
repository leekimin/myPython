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
"""
artist_1st_csv = pd.read_csv(
    artist_file_name, 
    encoding='UTF-8', 
    header=0,
    index_col=0, 
    dtype={'id':'string', 'track':'string', 'album':'string', 'track_id':'string', 'album_id':'string', 'album_year':'string'}
)

dict_tmp = []
artist_cnt = 0

# artist id 호출
for idx, row in artist_1st_csv.iterrows():
    artist_cnt = artist_cnt + 1
    print('-' * 50)
    print(artist_cnt, row['artist'])
    result_info = spo.search(q=row['artist'], limit=10, type='artist')
    info_cnt = 0
    for art in result_info['artists']['items']:
        info_cnt = info_cnt + 1
        dict_tmp.append(
            dict(
                artist=row['artist'],
                name=art['name'],
                id=art['id']
            )
        )
        " " "
        if row['artist'] == art['name']:
            print(art['name'], ',', art['id'])
            artist_1st_csv.at[idx, 'id'] = art['id']
        else:
            print('미일치 :', row['artist'], art['name'], art['id'])
        " " "
        print(info_cnt, 'Debug :', row['artist'], art['name'], art['id'])
        # 첫번째 ID를 우선 설정한다. 
        # 앨범 / 곡정보 체킹 후 해당 ID만 교체
        if info_cnt == 1:
            artist_1st_csv.at[idx, 'id'] = art['id']
        
    time.sleep(1) # 과다 호출 방지 ㅎㅎ
    #if artist_cnt == 1:
    #    break

# 1st에서 검색된 가수명으로 검색된 전체 목록 별도 저장
artist_2nd_csv = pd.DataFrame(dict_tmp)
artist_2nd_csv.to_csv('artist_all.csv')
"""

artist_csv = pd.read_csv(
    'artist_all.csv', 
    encoding='UTF-8', 
    header=0,
    index_col=0, 
    dtype={'id':'string', 'track':'string', 'album':'string', 'track_id':'string', 'album_id':'string', 'album_year':'string'}
)

dict_all = []

csv_cnt = 0
# 검색된 artist_id의 전체 앨범 목록 획득
for idx, row in artist_csv.iterrows():
    csv_cnt += 1
    
    if pd.isnull(row['id']) == True:
        print(idx, 'is null')
        continue
    else:
        print(idx, '-' * 40, 'start')

    print('progress :', csv_cnt, '/', len(artist_csv))
    
    # album, single 검색
    result_album = spo.artist_albums(artist_id=row['id'], limit=50, album_type='album,single')
    cnt = 0
    for alb in result_album['items']:
        cnt += 1
        print('album :', row['name'], '-- start', cnt, '/', len(result_album['items']))
        # album tracks 검색
        result_album_tracks = spo.album_tracks(album_id=alb['id'])
        for track in result_album_tracks['items']:
            dict_all.append(
                dict(
                    artist_id=row['id'],
                    artist_name=row['name'],
                    album_id=alb['id'],
                    album_name=alb['name'],
                    total_tracks=alb['total_tracks'],
                    release_date=alb['release_date'],
                    release_date_precision=alb['release_date_precision'],
                    album_type=alb['album_group'],
                    track_id=track['id'],
                    track_number=track['track_number'],
                    track_name=track['name']
                )
            )

pdDictAll = pd.DataFrame(dict_all)
pdDictAll.to_csv('artist_all_album.csv')

# 앨범 한개 1번 트랙만 가져와 1row에 넣기.. ( 정확도가 이상해 ㅡㅡㅋ )
# 제목도 이상함 ... 내가 원하는 정확한 제목을 해외 음워 API는 지원해주지 않는다. 
"""
cnt2 = 0
for idx, row in artist_csv.iterrows():
    if pd.isnull(row['id']) == True:
        continue

    print('-' * 50, 'start artist_albums :', row['id'])
    result_album = spo.artist_albums(artist_id=str(row['id']), limit=50, album_type=str('album,single'))
    cnt2 = cnt2 + 1
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
        
        artist_csv.at[idx, 'album'] = album_name
        artist_csv.at[idx, 'album_id'] = album_id
        artist_csv.at[idx, 'album_year'] = release_date
        break

    # artist_csv.at[idx, 'album_id']

    time.sleep(1)
    #result_top_tracks = spo.artist_top_tracks(artist_id='3sxWOFw4MSN54SIQ8np6iG')
    result_top_tracks = spo.artist_top_tracks(artist_id=row['id'])
    print('-' * 50, 'start artist_top_tracks')
    for top in result_top_tracks['tracks']:
        top_album = top['album']

        if artist_csv.at[idx, 'album_id'] == top_album['id']:
            result_album_tracks = spo.album_tracks(album_id=top_album['id'])
            #print(top_album['name'], top_album['release_date'], top['popularity'], top_album['id'])
            for tr in result_album_tracks['items']:
                print(top_album['name'], tr['track_number'], tr['name'])
                artist_csv.at[idx, 'track'] = tr['name']
                artist_csv.at[idx, 'track_id'] = tr['id']
                break

print('-' * 50, 'result csv')
print(artist_csv)
# 결과 저장
artist_csv.to_csv("artist_csv_first.csv")
print('-' * 50)
"""