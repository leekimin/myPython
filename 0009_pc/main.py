import requests
# html 파일 읽어서 원하는 문구 추출 후 csv 저장
from bs4 import BeautifulSoup
import pprint, os, datetime, re, sys, copy
import pandas as pd

# html 파일 목록 찾기
path = "./Windows/"
path_txt = "./Windows/"
file_list1 = os.listdir(path)
file_list2 = os.listdir(path_txt)
file_list_html = [file for file in file_list1 if file.endswith(".html")]
file_list_txt = [file for file in file_list2 if file.endswith(".txt")]

# 파일명 리스트 -> PC 스펙 정보로 문자열 취합
# "a":{"cpu":"i7-1290KF", "gpu":"RTX 4070 Ti"} -> 이 형태로 만들고, CSV로 생성
stansPc = {
    
}

# key는 파일명 ( 직원명 or 서버명 포함이라 기준 삼음 )
for f in file_list1:
    stansPc[f] = {}

"""
stansPc["경영실_대여PC_2020-D-016.txt"] = {"cpu":"i7-1290KF", "gpu":"RTX 4070\r Ti"}

p = pd.DataFrame.from_dict(stansPc)
p.transpose()
pprint.pprint(p.transpose())

now = datetime.datetime.now()
formatted_date = now.strftime("PC_%Y%m%d%H%M%S.csv")
csv_file_name = formatted_date

p.transpose().to_csv("./" + csv_file_name, encoding="CP949")

sys.exit("Test 종료")
"""

# 찾을 문자열 Dictionary
dicSearch = {
    "ComName":"컴퓨터 이름:",                   # O
    "ComBrand":"컴퓨터 브랜드:",                # O
    "OS":"운영 체제:",                          # O
    "User":"현재 사용자 이름:",                 # O
    #"CpuCnt":"프로세서 패키지 수(물리적):",
    "CpuBrand":"CPU 브랜드:",                   # O
    #"CpuCore":"프로세서 코어 수:",
    #"CpuThread":"논리 프로세서 수:",
    #"ProcessorName":"프로세서 이름:",
    "MainboardModel":"마더보드 모델:",           # O
    "MainboardChipset":"마더보드 칩셋:",         # O
    #"BiosBender":"BIOS 제조업체:",
    "Battery":"설계된 용량:",                    # O
    "Memory":"총 메모리 크기:",                  # O
    "MemoryChannel":"지원되는 메모리 채널:",      # O
    "MemoryActive":"활성 메모리 채널:",           # O
    "GpuName":"그래픽 칩셋:",                    # O
    #"GpuCard":"그래픽 카드:",
    "Monitor":"모니터 이름(제조업체):",           # O
    "DriveModel":"드라이브 모델:",
    "DriveSize":"드라이브 용량:",
    "NetworkCard":"네트워크 카드:",
    #"NetworkSpeed":"최대 링크 속도:",
}

dicEngSearch = {
    "ComName":"Computer Name:", # "컴퓨터 이름:",
    "ComBrand":"Computer Brand Name:", #"컴퓨터 브랜드:",
    "OS":"Operating System:", #"운영 체제:",
    "User":"Current User Name:", #"현재 사용자 이름:",
    #"CpuCnt":"프로세서 패키지 수(물리적):",
    "CpuBrand":"CPU Brand Name:", #"CPU 브랜드:",
    #"CpuCore":"프로세서 코어 수:",
    #"CpuThread":"논리 프로세서 수:",
    #"ProcessorName":"프로세서 이름:",
    "MainboardModel":"Motherboard Model:", #"마더보드 모델:",
    "MainboardChipset":"Motherboard Chipset:", #"마더보드 칩셋:",
    #"BiosBender":"BIOS 제조업체:",
    "Battery":"Designed Capacity:", #"설계 용량:",
    "Memory":"Total Memory Size:", #"총 메모리 크기:",
    "MemoryChannel":"Memory Channels Supported:", #"지원되는 메모리 채널:",
    "MemoryActive":"Memory Channels Active:", #"활성 메모리 채널:",
    "GpuName":"Video Chipset:", #"그래픽 칩셋:",
    #"GpuCard":"그래픽 카드:",
    "Monitor":"Monitor Name (Manuf):", #"모니터 이름(제조업체):",
    "DriveModel":"Drive Model:", #"드라이브 모델:",
    "DriveSize":"Drive Capacity:", #"드라이브 용량:",
    "NetworkCard":"Network Card:", #"네트워크 카드:",
    #"NetworkSpeed":"최대 링크 속도:",
}

dicLinuxSearch = {
    "ComName":"Icon name:", # "컴퓨터 이름:",
    "ComBrand":"Computer Brand Name:", #"컴퓨터 브랜드:",
    "OS":"Operating System:", #"운영 체제:",
    "User":"Static hostname:", #"현재 사용자 이름:",
    #"CpuCnt":"프로세서 패키지 수(물리적):",
    "CpuBrand":"model name	:", #"CPU 브랜드:",
    #"CpuCore":"프로세서 코어 수:",
    #"CpuThread":"논리 프로세서 수:",
    #"ProcessorName":"프로세서 이름:",
    "MainboardModel":"Motherboard Model:", #"마더보드 모델:",
    "MainboardChipset":"Motherboard Chipset:", #"마더보드 칩셋:",
    #"BiosBender":"BIOS 제조업체:",
    #"Battery":"Designed Capacity:", #"설계 용량:",
    "Memory":"Memory Size:", #"총 메모리 크기:",
    "MemoryChannel":"Memory Channels Supported:", #"지원되는 메모리 채널:",
    "MemoryActive":"Memory Channels Active:", #"활성 메모리 채널:",
    "GpuName":"Video Chipset:", #"그래픽 칩셋:",
    #"GpuCard":"그래픽 카드:",
    "Monitor":"Monitor Name (Manuf):", #"모니터 이름(제조업체):",
    "DriveModel":"Drive Model:", #"드라이브 모델:",
    "DriveSize":"Drive Capacity:", #"드라이브 용량:",
    "NetworkCard":"Network Card:", #"네트워크 카드:",
    #"NetworkSpeed":"최대 링크 속도:",
}


# 스탠스 관리 항목으로 추출해보자...
dicStansSearch = {
    "No":"no",
    "부서":"",
    "이름":"",
    "모니터":"",
    "데스크탑 여부":"",
    "랩탑":"",
    "컴퓨터 브랜드":"",
    "태블릿":"",
    "휴대폰":"",
    "이동식 디스크":"",
    "운영 체제":"",
    "MSOffice":"",
    "한글":"",
    "AdobeCC":"",
    "Unity":"",
    "Figma":"",
    "MAYA":"",
    "Amold":"",
    "Zbrush":"",
    "3DMAX":"",
    "SubstancePainter":"",
    "기타 프로그램":"",
    "관리자":"",
    "PCSpec":"PC 스펙",
    "PC 업데이트 사항":"",
    "PC 부속품 업데이트 요청":"",
}

pc_list = {}
stans_list = {}

def getText(str):
    return BeautifulSoup(str, "html.parser")

def getKeyCount(dic, key):
    cnts = 0
    for k in dic:
        if key in k:
            cnts = cnts + 1
    return str(cnts)

# Windows 계열
def getHtmlParsing(html):
    f = open(path + html, "r", encoding="utf-8")
    lines = f.readlines()
    f.close()
    dic = {}
    dic_stans = {}
    ccc = 0
    for line in lines:
        for key in dicSearch:
            ccc = ccc + 1
            if dicSearch[key] in line:
                dic_new_key = dicSearch[key].replace(':', '')
                cnt = dic.get(dic_new_key, 0)

                # 존재하는 키는 키 값에 숫자 붙여준다.
                if type(cnt) is str:
                    dic_new_key = dic_new_key + getKeyCount(dic, dic_new_key)

                dic[dic_new_key] = getText(line).text.strip().split(':')[1]

            if dicSearch[key] in line:
                dic_new_key = dicSearch[key].replace(':', '')
                cnt = dic_stans.get(dic_new_key, 0)

                if type(cnt) is str:
                    dic_stans[dic_new_key] = dic_stans[dic_new_key] + " \n" + getText(line).text.strip().split(':')[1]
                else:
                    dic_stans[dic_new_key] = getText(line).text.strip().split(':')[1]

        for key in dicEngSearch:
            if dicEngSearch[key] in line:
                dic_new_key = dicEngSearch[key].replace(':', '')
                dic_new_key = dicSearch[key].replace(':', '')
                cnt = dic.get(dic_new_key, 0)

                # 존재하는 키는 키 값에 숫자 붙여준다.
                if type(cnt) is str:
                    dic_new_key = dic_new_key + getKeyCount(dic, dic_new_key)

                dic[dic_new_key] = getText(line).text.strip().split(':')[1]

            if dicEngSearch[key] in line:
                dic_new_key = dicEngSearch[key].replace(':', '')
                dic_new_key = dicSearch[key].replace(':', '')
                cnt = dic_stans.get(dic_new_key, 0)

                if type(cnt) is str:
                    dic_stans[dic_new_key] = dic_stans[dic_new_key] + " \n" + getText(line).text.strip().split(':')[1]
                else:
                    dic_stans[dic_new_key] = getText(line).text.strip().split(':')[1]
    
    pc_list[html] = dic

    #pprint.pprint(dic_stans)

    dicStansSearchBackup = copy.deepcopy(dicStansSearch)

    for key in dic_stans:
        # dicStansSearch에 key가 없으면 PCSpec에 줄바꿈으로 등록
        #print(key, dic_stans[key])

        chk = dicStansSearchBackup.get(key, 0)
        if type(chk) is str:
            dicStansSearchBackup[key] = dic_stans[key]
        else:
            dicStansSearchBackup['PCSpec'] = dicStansSearchBackup['PCSpec'] + ' \n\t' + key + ' : ' + dic_stans[key]

    # 가공해서 넣기
    stans_list[html] = dicStansSearchBackup

    # dicStansSearch = copy.deepcopy(dicStansSearchBackup)

# 부품별 정규식 추출
def getRegxDeviceName(strRegx, allTxt, idx):
    sMatch = re.findall(strRegx, allTxt)
    deviceName = ""

    for m in sMatch:
        # print(m)
        deviceName = m[idx]
        if idx == 3:
            break

    return deviceName

# Ubuntu 계열
def getTextParsing(txt):
    f = open(path_txt + txt, "r", encoding="utf-8")
    lines_txt = f.readlines()
    f.close()

    dic_stans = {}
    dic = {}

    # 전체 문자열( 정규식 찾기 위함 )
    allTxt = ''.join(lines_txt)

    # 중복은 제거할 키값 Temp ( 아래 값이 여러번 나와서 continue 시킴 )
    dup_key = ['CPU 브랜드']

    # 여러개도 고려해야함
    # 그래픽 카드 start
    strRegx = r'Hardware Class: graphics car(.+)(\s+)(.+)(\s+)Model: \"(.+)\"'
    dic_new_key = dicSearch['GpuName'].replace(':', '')
    dic[dic_new_key] = getRegxDeviceName(strRegx, allTxt, 4)
    dic_stans[dic_new_key] = getRegxDeviceName(strRegx, allTxt, 4)
    # 그래픽 카드 end

    # 여러개도 고려해야함
    # Disk start
    strRegx = r'Hardware Class: dis(.+)(\s+)(.+)(\s+)Model: \"(.+)\"'
    dic_new_key = dicSearch['DriveModel'].replace(':', '')
    dic[dic_new_key] = getRegxDeviceName(strRegx, allTxt, 4)
    dic_stans[dic_new_key] = getRegxDeviceName(strRegx, allTxt, 4)
    # Disk end

    # network start
    strRegx = r'Hardware Class: network(\s+)(.+)(\s+)Model: \"(.+)\"'
    dic_new_key = dicSearch['NetworkCard'].replace(':', '')
    dic[dic_new_key] = getRegxDeviceName(strRegx, allTxt, 3)
    dic_stans[dic_new_key] = getRegxDeviceName(strRegx, allTxt, 3)
    # network end

    # monitor start
    strRegx = r'Hardware Class: monitor(\s+)(.+)(\s+)Model: \"(.+)\"'
    dic_new_key = dicSearch['Monitor'].replace(':', '')
    dic[dic_new_key] = getRegxDeviceName(strRegx, allTxt, 3)
    dic_stans[dic_new_key] = getRegxDeviceName(strRegx, allTxt, 3)
    # monitor end

    # Mainboard start
    # 여기 정보가 이상하네 ( 나중에 추출 스크립트 다시 작성 ) - 구분이 다르게 뽑히네..( 고민 .. )
    strRegx = r'MODALIAS(.)+rn(.+):rvr'
    strRegx2 = r'MODALIAS(.)+SystemVersion:rvn(.+):rn'
    dic_new_key = dicSearch['MainboardModel'].replace(':', '')
    dic[dic_new_key] = getRegxDeviceName(strRegx2, allTxt, 1) + ' ' + getRegxDeviceName(strRegx, allTxt, 1)
    dic_stans[dic_new_key] = getRegxDeviceName(strRegx2, allTxt, 1) + ' ' + getRegxDeviceName(strRegx, allTxt, 1)
    # Mainboard end

    for line in lines_txt:
        for key in dicLinuxSearch:
            
            if dicLinuxSearch[key] in line:
                dic_new_key = dicLinuxSearch[key].replace(':', '')
                dic_new_key = dicSearch[key].replace(':', '')
                cnt = dic.get(dic_new_key, 0)

                # 존재하는 키는 키 값에 숫자 붙여준다.
                if type(cnt) is str:
                    if dic_new_key in dup_key:
                        continue
                    dic_new_key = dic_new_key + getKeyCount(dic, dic_new_key)

                dic[dic_new_key] = getText(line).text.strip().split(':')[1]
        
            if dicLinuxSearch[key] in line:
                dic_new_key = dicLinuxSearch[key].replace(':', '')
                dic_new_key = dicSearch[key].replace(':', '')
                cnt = dic_stans.get(dic_new_key, 0)

                if type(cnt) is str:
                    dic_stans[dic_new_key] = dic_stans[dic_new_key] + " \n" + getText(line).text.strip().split(':')[1]
                else:
                    dic_stans[dic_new_key] = getText(line).text.strip().split(':')[1]
        
        for key in dicEngSearch:
            if dicEngSearch[key] in line:
                dic_new_key = dicEngSearch[key].replace(':', '')
                cnt = dic_stans.get(dic_new_key, 0)
                print("dic_new_key : ", dic_new_key)

                if type(cnt) is str:
                    dic_stans[dic_new_key] = dic_stans[dic_new_key] + " \n" + getText(line).text.strip().split(':')[1]
                else:
                    dic_stans[dic_new_key] = getText(line).text.strip().split(':')[1]
        
    pc_list[txt] = dic

    # 리스트 재정리
    # stans_list[txt]
    dicStansSearchBackup = copy.deepcopy(dicStansSearch)

    for key in dic_stans:
        # dicStansSearch에 key가 없으면 PCSpec에 줄바꿈으로 등록
        #print(key, dic_stans[key])

        chk = dicStansSearchBackup.get(key, 0)
        if type(chk) is str:
            dicStansSearchBackup[key] = dic_stans[key]
        else:
            dicStansSearchBackup['PCSpec'] = dicStansSearchBackup['PCSpec'] + ' \n\t' + key + ' : ' + dic_stans[key]

    # 가공해서 넣기
    stans_list[txt] = dicStansSearchBackup


# 파일별로 추출하기..( 윈도우에서 출력한 파일만 처리 )
for html in file_list_html:
    #if html == "경영지원실_신성희.html":
        print('*' * 50, html)
        getHtmlParsing(html) # Windows 계열
        #print(stans_list)

        print('*' * 50, 'end')

# print(stans_list)

for txt in file_list_txt:
    # 잘못 추출했다.. 정규식 쓰자..
    #if txt == "딥러닝엔진개발팀_학습서버.txt":
        print('*' * 50, txt)
        getTextParsing(txt) # Linux 계열
        print('*' * 50, 'end')

""" 정규식 테스트
f = open(path_txt + txt, "r", encoding="utf-8")
rline = f.readlines()
f.close()

str = ''.join(rline)

# Graphic Card 모델명 찾기
strRegx = r'Hardware Class: graphics car(.+)(\s+)(.+)(\s+)Model: \"(.+)\"'
strMatch = re.findall(strRegx, str)

print('*' * 10, 'start')
for m in strMatch:
    print(m[4])

print('*' * 10, 'end')
"""

# Ubuntu 계열은 파일 내용 보고 다시 파싱
#print(pc_list)

p = pd.DataFrame(stans_list)
# pprint.pprint(p)

now = datetime.datetime.now()
formatted_date = now.strftime("PC_%Y%m%d%H%M%S.csv")
csv_file_name = formatted_date

p.transpose().to_csv("./" + csv_file_name, encoding="CP949")


