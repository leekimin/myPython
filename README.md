# myPython

파이썬 학습

## 로그 파일에서 원하는 항목을 정규식으로 추출해서 문자열 조합하기(csv 만들기)

```
>> 0001_first_sample\main.py
함수 선언
py 파일 import
정규식
배열 및 join
file open 및 생성, 쓰기
```

## PDF

```
>> 0002_pdf
PDF 생성 해보자
```

## 기본 문법

```
>> 0003_basic
문법 테스트용
```

## OCR

```
>> 0004_ocr
OCR 이용해 보기
```

## MP3, Flac Tag 일괄수정

```
>> 0005_mp3_tag
eyed3
pylast - last.fm api
http://www.maniadb.com/api/search/metallica/?sr=artist&display=10&key=example&v=0.5 - api
Path
```

### 시나리오

1. 저장 디스크 특정 경로 하위에 존재하는 모든 폴더 목록 추출( 1st.py )

    - 전체 경로는 개인별 편차가 존재
    - 검색해야할 artist 명을 폴더 depth로 수기 작업하여 리스트업
    - csv 파일로 저장

1. 가수명의 spotify 정보 조회( 2nd.py )

    - 1st의 csv 파일의 가수명으로 id, 대표곡 조회
    - csv 파일로 저장 후 엑셀로 수기 필터링

1. 정리된 가수의 앨범, 싱글, 트랙 정보 조회( 3rd.py )

    - spotify api로 정보 획득 후 csv 저장
    - 미존재 앨범은 flag 수기 작업 후 csv 수정

1. 저장 폴더 하위의 mp3, flac 파일 전체 조회( 4th.py )

    - eyed3로 태그가 존재하지 않는 파일 선별 / 깨진 태그 정보 선별
    - 3rd.py에서 생성한 csv 리스트에서 track 정보 검색
    - eyed3 태그 조회 후 수정
