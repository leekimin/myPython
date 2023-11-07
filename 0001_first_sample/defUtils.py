import re

"""
sourceFilePath 파일의 내용은 cat 명령어로 추출된 1차 가공데이터
"""

# logStatus start...
def logStatus(sourceFilePath, extractFilePath):
    print('wdd_Status_Verify... 로그 추출')
    sourceFile = open(sourceFilePath)

    line_num = 1
    line = sourceFile.readline()

    while line:
        # To-Do
        extractFile = open(extractFilePath, "a+") # 없으면 생성 후 오픈

        # 정규식으로 로그시간, 참여자코드, 학회시퀀스, 세션시퀀스 추출
        no1Tmp = line[0:23] # 로그 시간
        no2Tmp = re.findall(r'Wdd_Ses_UID=[0-9]+', line) # 참여자 코드
        no3Tmp = re.findall(r'Wdd_Ses_SympSEQ=[0-9]+', line) # 학회 시퀀스
        no4Tmp = re.findall(r'\SESS_SEQ -> \([0-9]+\)', line) # 세션 시퀀스

        no1 = ''
        no2 = ''
        no3 = ''
        no4 = ''
        
        # 추출된 문자열 치환
        no1 = no1Tmp
        if len(no2Tmp) > 0:
            no2 = no2Tmp[0]
            no2 = no2.replace('Wdd_Ses_UID=', '')
        if len(no3Tmp) > 0:
            no3 = no3Tmp[0]
            no3 = no3.replace('Wdd_Ses_SympSEQ=', '')
        if len(no4Tmp) > 0:
            no4 = no4Tmp[0]
            no4 = no4.replace('SESS_SEQ -> (' ,'')
            no4 = no4.replace(')', '')

        # 진행 상황 로깅 넘버링
        if line_num % 100 == 0:
            print(line_num)

        log = [no1, no2, no3, no4]; # append pop remove로 가능

        # 추출 문서에 기록
        extractFile.write(','.join(log) + "\n")
        extractFile.close()

        line = sourceFile.readline()
        line_num += 1

    sourceFile.close()
# logStatus end...

# logAttendSave start...
def logAttendSave(sourceFilePath, extractFilePath):
    print('입퇴장 기록 로그용')

    sourceFile = open(sourceFilePath)

    line_num = 1
    line = sourceFile.readline()

    while line:
        extractFile = open(extractFilePath, "a+") # 없으면 생성 후 오픈

        # 정규식으로 로그시간, 참여자코드, 학회시퀀스, 세션시퀀스, 입퇴장여부 추출
        no1Tmp = line[0:23] # 로그 시간
        no2Tmp = re.findall(r'Wdd_Ses_UID=[0-9]+', line) # 참여자 코드
        no3Tmp = re.findall(r'Wdd_Ses_SympSEQ=[0-9]+', line) # 학회 시퀀스
        no4Tmp = re.findall(r'\SESS_SEQ\"\:[0-9]+', line) # 세션 시퀀스
        no5Tmp = re.findall(r'InYN\"\:\"[YN]\"', line)

        no1 = ''
        no2 = ''
        no3 = ''
        no4 = ''
        no5 = ''

        # 추출된 문자열 치환
        no1 = no1Tmp
        if len(no2Tmp) > 0:
            no2 = no2Tmp[0]
            no2 = no2.replace('Wdd_Ses_UID=', '')
        if len(no3Tmp) > 0:
            no3 = no3Tmp[0]
            no3 = no3.replace('Wdd_Ses_SympSEQ=', '')
        if len(no4Tmp) > 0:
            no4 = no4Tmp[0]
            no4 = no4.replace('SESS_SEQ":' ,'')
        if len(no5Tmp) > 0:
            no5 = no5Tmp[0]
            no5 = no5.replace('"', '')
            no5 = no5.replace('InYN:', '')

        # 진행 상황 로깅 넘버링
        if line_num % 100 == 0:
            print(line_num)

        log = [no1, no2, no3, no4, no5];

        # 추출 문서에 기록( 3가지 항목이 없을수 있는건 제외)
        if len(no2Tmp) > 0 or len(no3Tmp) > 0 or len(no4Tmp) > 0 or len(no5Tmp) > 0:
            extractFile.write(','.join(log) + "\n")
        
        extractFile.close()
        
        line = sourceFile.readline()
        line_num += 1

    sourceFile.close()
# logAttendSave end...