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

    sourceFileTotal = open(sourceFilePath)
    total_line = len(sourceFileTotal.readlines())
    sourceFileTotal.close()

    # To-Do
    extractFile = open(extractFilePath, "a+") # 없으면 생성 후 오픈

    while line:
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
            print(line_num , ' / ' , total_line)

        log = [no1, no2, no3, no4]; # append pop remove로 가능

        # 추출 문서에 기록
        extractFile.write(','.join(log) + "\n")

        line = sourceFile.readline()
        line_num += 1

    extractFile.close()
    sourceFile.close()
# logStatus end...

# logAttendSave start...
def logAttendSave(sourceFilePath, extractFilePath):
    print('입퇴장 기록 로그용')

    sourceFile = open(sourceFilePath)

    line_num = 1
    line = sourceFile.readline()

    sourceFileTotal = open(sourceFilePath)
    total_line = len(sourceFileTotal.readlines())
    sourceFileTotal.close()

    extractFile = open(extractFilePath, "a+") # 없으면 생성 후 오픈

    while line:
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
            print(line_num , ' / ' , total_line)

        log = [no1, no2, no3, no4, no5];

        # 추출 문서에 기록( 3가지 항목이 없을수 있는건 제외)
        if len(no2Tmp) > 0 or len(no3Tmp) > 0 or len(no4Tmp) > 0 or len(no5Tmp) > 0:
            extractFile.write(','.join(log) + "\n")
        
        line = sourceFile.readline()
        line_num += 1

    extractFile.close()
    sourceFile.close()
# logAttendSave end...

# 학회 코드에 맞는 분리 파일명 조합
def logTargetName(basePath, logFileName, arrTarget, line):
    fileName = ''

    # 예외는 일단 패스... 다 담긴걸로 판단
    for d in arrTarget:
        if (line.find(d) > -1):
            fileName = d

    return basePath + logFileName + fileName + '.csv'

# 코드별 파일 생성 및 내용 추가
def logSplitConf(basePath, sourceFile, logFileName, *targetName):
    print('학회별 로그 분리')

    sourceFilePath = basePath + '' + sourceFile

    sourceFile = open(sourceFilePath)

    line_num = 1
    line = sourceFile.readline()
    
    sourceFileTotal = open(sourceFilePath)
    total_line = len(sourceFileTotal.readlines())
    print (total_line)
    sourceFileTotal.close()

    while line:
        # 분리할 파일명 생성
        extractFile = open(logTargetName(basePath, logFileName, targetName, line), "a+")
        
        # 진행 상황 로깅 넘버링
        if line_num % 100 == 0:
            print(line_num , ' / ' , total_line)

        extractFile.write(line)
        extractFile.close()
        
        line = sourceFile.readline()
        line_num += 1

    sourceFile.close()