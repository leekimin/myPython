import requests
# html 파일 읽어서 원하는 문구 추출 후 csv 저장
from bs4 import BeautifulSoup
import pprint, os, datetime
import pandas as pd

# html 파일 목록 찾기
path = "./"
file_list = os.listdir(path)
file_list_html = [file for file in file_list if file.endswith(".html")]

# 찾을 문자열 Dictionary
dicSearch = {
    "ComName":"컴퓨터 이름:",
    "ComBrand":"컴퓨터 브랜드:",
    "OS":"운영 체제:",
    "User":"현재 사용자 이름:",
    #"CpuCnt":"프로세서 패키지 수(물리적):",
    "CpuBrand":"CPU 브랜드:",
    #"CpuCore":"프로세서 코어 수:",
    #"CpuThread":"논리 프로세서 수:",
    #"ProcessorName":"프로세서 이름:",
    "MainboardModel":"마더보드 모델:",
    "MainboardChipset":"마더보드 칩셋:",
    #"BiosBender":"BIOS 제조업체:",
    "Battery":"설계 용량:",
    "Memory":"총 메모리 크기:",
    "MemoryChannel":"지원되는 메모리 채널:",
    "MemoryActive":"활성 메모리 채널:",
    "GpuName":"그래픽 칩셋:",
    #"GpuCard":"그래픽 카드:",
    "Monitor":"모니터 이름(제조업체):",
    "DriveModel":"드라이브 모델:",
    "DriveSize":"드라이브 용량:",
    "NetworkCard":"네트워크 카드:",
    #"NetworkSpeed":"최대 링크 속도:",
}

pc_list = {}

def getText(str):
    return BeautifulSoup(str, "html.parser")

def getKeyCount(dic, key):
    cnts = 0
    for k in dic:
        if key in k:
            cnts = cnts + 1
    return str(cnts)

def getHtmlParsing(html):
    f = open(html, "r", encoding="utf-8")
    lines = f.readlines()
    f.close()
    dic = {}
    for line in lines:
        for key in dicSearch:
            if dicSearch[key] in line:
                dic_new_key = dicSearch[key].replace(':', '')
                cnt = dic.get(dic_new_key, 0)

                # 존재하는 키는 키 값에 숫자 붙여준다.
                if type(cnt) is str:
                    dic_new_key = dic_new_key + getKeyCount(dic, dic_new_key)

                dic[dic_new_key] = getText(line).text.strip().split(':')[1]
    
    pc_list[html] = dic

# 파일별로 추출하기..( 윈도우에서 출력한 파일만 처리 )
for html in file_list_html:
    print('*' * 50, html)
    getHtmlParsing(html)
    print('*' * 50, 'end')

# Ubuntu 계열은 파일 내용 보고 다시 파싱

#print(pc_list)

p = pd.DataFrame(pc_list)
pprint.pprint(p)

now = datetime.datetime.now()
formatted_date = now.strftime("PC_%Y%m%d%H%M%S.csv")
csv_file_name = formatted_date

p.to_csv("./" + csv_file_name, encoding="CP949")


