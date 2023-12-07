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

1. 저장 디스크 특정 경로 하위에 존재하는 모든 mp3, flac 목록 뽑아내기

    - 전체 경로는 개인별 편차가 존재

1. 가수, 앨범, 제목을 추출하기

    - 비정리 상태라 난이도 높음
    - 가수 - 앨범명 - 제목
    - 가수 - 앨범.zip
    - 가수 - 제목

1. eyed3로 mp3의 Tag 정보 조회

    - 한글이 깨진 상태로 조회 되는 파일들

1. API로 Track 정보 획득

    - 검색 정확도 이슈

1. eyed3로 읽은 태그 정보 업데이트
