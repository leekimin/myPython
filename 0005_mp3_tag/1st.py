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
print(f'rootPath : {rootPath}, depths : {depth}')
print('=' * 50, '')

# 디렉토리 폴더명(가수명) 조회
listdirs(rootPath)

artist_tmp_file_name = 'artists_tmp.csv'

tempcsv = None

try:
    tempcsv = pd.read_csv(artist_tmp_file_name, encoding='UTF-8', header=None, index_col=0)
    print(tempcsv.dtypes)
    print(type(tempcsv))
    print('-' * 50)
except:
    print('파일 내용 없음')
    tempcsv = pd.DataFrame(None)

dictArtists = []

for d in arrFolderList:
    depth_tmp = len(d.full_path.split('\\'))
    if depth_tmp == 4:
        # print(d.artist, d.full_path, depth_tmp)
        dictArtists.append(
            dict(
                artist=d.artist,
                id=''
            )
        )
        

# print(tempcsv)

dtFrame = pd.DataFrame(dictArtists)
print(dtFrame)

dtFrame.to_csv(artist_tmp_file_name)

# https://skillmemory.tistory.com/entry/Pandas-1-csv-%EB%8D%B0%EC%9D%B4%ED%83%80-%EC%9D%BD%EA%B3%A0-%EC%B2%98%EB%A6%AC-%EC%B6%94%EA%B0%80-%EC%A0%80%EC%9E%A5
# 폴더 목록 조회
# 폴더 레벨에 따른 가수명 수집
# csv 파일 생성 및 수정