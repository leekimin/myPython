"""
1. 저장 디스크 특정 경로 하위에 존재하는 모든 폴더 목록 추출( 1st.py )
    - 전체 경로는 개인별 편차가 존재
    - 검색해야할 artist 명을 폴더 depth로 수기 작업하여 리스트업
    - csv 파일로 저장
"""
import sys, os
import pprint
from func import arrFileList, arrFolderList, listdirs, Music
import pandas as pd
from pandas import DataFrame

# argv : 루트경로, *depth(위치-배열)

if len(sys.argv) != 3:
    print('parameter error')
    exit()

# depth는 int만 허용
try:
    t = int(sys.argv[2])
except:
    print(f'not int type > argument {sys.argv[2]}')
    exit()

rootPath = sys.argv[1]
depth = int(sys.argv[2])

# D:\_my\sample\
print('=' * 50, '')
print(f'artist collect > rootPath : {rootPath}, depths : {depth}')
print('=' * 50, '')

# 디렉토리 폴더명(가수명) 조회
listdirs(rootPath)

# 생성할 파일명 (csv)
artist_tmp_file_name = 'artists_tmp.csv'

try:
    artist_csv = pd.read_csv(artist_tmp_file_name, encoding='UTF-8', header=0, index_col=0)
    #print(artist_csv.dtypes)
    #print(type(artist_csv))
    #print('-' * 50)
except:
    print('Msg > new File Create')
    artist_csv = pd.DataFrame(None)

# 폴더명에서 데이터 검색
for d in arrFolderList:
    depth_tmp = len(d.full_path.split('\\'))
    if depth_tmp == 4:
        # Data가 없으면 key가 없어서 분기 처리
        if len(artist_csv) == 0:
            #print('첫 데이터는 append')
            row_tmp = pd.DataFrame([{"artist":d.artist, "id":"", "track":"", "album":""}])
            artist_csv = pd.concat([artist_csv, row_tmp], ignore_index=True)
        else:
            #print('중복 체크 후 append')
            is_exists = artist_csv['artist'] == d.artist
            if len(artist_csv[is_exists]) == 0:
                row_tmp = pd.DataFrame([{"artist":d.artist, "id":"", "track":"", "album":""}])
                artist_csv = pd.concat([artist_csv, row_tmp], ignore_index=True)

print('총 카운트 :', len(artist_csv))
print('=' * 50)

artist_csv.to_csv(artist_tmp_file_name)

# https://skillmemory.tistory.com/entry/Pandas-1-csv-%EB%8D%B0%EC%9D%B4%ED%83%80-%EC%9D%BD%EA%B3%A0-%EC%B2%98%EB%A6%AC-%EC%B6%94%EA%B0%80-%EC%A0%80%EC%9E%A5
# 폴더 목록 조회
# 폴더 레벨에 따른 가수명 수집
# csv 파일 생성 및 수정


# pip install eyed3
# pip install pandas