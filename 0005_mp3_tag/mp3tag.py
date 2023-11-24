import eyed3
import requests
import json

mp3 = eyed3.load("Hoobastank - The Reason.mp3")

print("*" * 30)
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
        print("response status %r" % response.status_code)
        print("response text %r" % response.text)
    except Exception as ex:
        print(ex)


# https://github.com/pylast/pylast

send_api('', 'GET')
