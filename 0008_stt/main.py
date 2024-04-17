import requests
filename = "D:\\study\\myPython\\0008_stt\\sample.m4a" 
def read_file(filename, chunk_size=5242880): 
    with open(filename, 'rb') as _file: 
        while True: 
            data = _file.read(chunk_size) 
            if not data: 
                break 
            yield data 

headers = {'authorization': "06708306b992491cbb1ad9dfae200e89"} 
response = requests.post('https://api.assemblyai.com/v2/upload', headers=headers, data=read_file(filename)) 

print(response.json())