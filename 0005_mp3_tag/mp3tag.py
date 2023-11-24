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
