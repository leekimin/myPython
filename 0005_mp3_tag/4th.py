"""
1. 저장 폴더 하위의 mp3, flac 파일 전체 조회( 4th.py )
    - eyed3로 태그가 존재하지 않는 파일 선별 / 깨진 태그 정보 선별
    - 3rd.py에서 생성한 csv 리스트에서 track 정보 검색
    - eyed3 태그 조회 후 수정
"""
# 폴더 하위 파일 전체 리스트업
# 3rd에서 준비한 시트에서 정보 검색
# tag 일괄 수정
import sys, eyed3, json, time, pprint
from func import arrFileList, arrFolderList, listdirs, Music, track_info
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

eyed3.log.setLevel("ERROR")

# argv : 검색루트경로
if len(sys.argv) != 2:
    print('parameter error')
    exit()

# mp3, flac 검색 최상위 경로
rootPath = sys.argv[1]

listdirs(rootPath)

total_tracks_cnt = len(arrFileList)
print('# 전체 곡수 :', total_tracks_cnt)

track_data_file = 'artist_all_album.csv'

# 2nd에서 정리한 전체 곡 정보 데이터
artist_2nd_csv = pd.read_csv(
    track_data_file, 
    encoding='UTF-8', 
    header=0,
    index_col=0, 
    dtype={
        'id':'string', 'track':'string', 'album':'string', 'track_id':'string', 
        'album_id':'string', 'album_year':'string', 'use_yn':'string'
    }
)

# 2nd에서 수집한 데이터에서 사용여부를 수기 작업한 목록만 메모리에 올려놓는다.
# 해당 자료에서 데이터 검색 후 mp3tag를 업데이트 함
artist_2nd_data = artist_2nd_csv[artist_2nd_csv["use_yn"] == "Y"]
# pprint.pprint(artist_2nd_data)

for f in arrFileList:
    print('-' * 50, 'track info')
    track_nm = f.track
    track_path = f.full_path
    print(track_path)

    mp3 = eyed3.load(track_path)
    #track_info(track_path)
    print('Header Version :', mp3.tag.header.version)
    print('isV1 :', mp3.tag.isV1())
    print('isV2 :', mp3.tag.isV2())
    
    # 앨범 커버 등록 ( file open or url open)
    if len(mp3.tag.images) > 0:
        print('image cover exist')
    else:
        print('not found image cover')

    # Track Name
    # Track Images
    # Track Artist
    # Track Album
    # Track Number
    # Album Artist
    # Album Year
    # Album Recoding Date
    
    # image delete
    #mp3.tag.images.remove(u'')
    """
    # image add from file
    img_tmp = open('cover.png', 'rb')
    mp3.tag.images.set(3, img_tmp.read(), 'image/png', u'')
    #mp3_tmp.tag.images.set(3, '', '', u'', 'http://localhost:8800/test.png')
    """
    #mp3.tag.save()

    # 검색 방법
    rows = artist_2nd_data[artist_2nd_data["track_name"].str.upper().str.contains(track_nm.upper())]
    print('-' * 50, 'search count :', len(rows), track_nm)
    # 한곡만 검색되는 경우만 tag 업데이트
    if len(rows) != 1:
        print('skip...')
        continue

    for idx, row in rows.iterrows():
        print(
            row["track_name"], row["artist_name"], row['album_name'], row['track_number'],
            row['release_date'], row['release_date_precision']
        )
    
    # ,artist_id,artist_name,album_id,album_name,total_tracks,
    # ,release_date,release_date_precision,album_type,track_id
    # ,track_number,track_name,use_yn
exit()







