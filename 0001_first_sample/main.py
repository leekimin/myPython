from defUtils import logStatus, logAttendSave, logSplitConf, StopWatch
import sys, os, platform

print("-" * 88)

"""
logStatus('D:\\_my\\test.txt', 'D:\\_my\\testResult.txt')
logAttendSave('D:\\_my\\test.txt', 'D:\\_my\\testResult.txt')
"""

stopwatch = StopWatch()
stopwatch.start()

if len(sys.argv) == 1:
    print('입력인자 필수 > python3 main.py filename')
    exit()

target_file = sys.argv[1]

# 대상 로그에서 1차 데이터 추출
# os.system('linux command execute')

# 파일하나로 머지
#basePath = r'D:\\_my\\1105_conf\\20231203\\'
basePath = r'/var/log/app/tomcat/wapi/extractpy/'

# 로그 취합할 하나의 로그 파일명
makeFileName = 'wLog_Total.csv'
makeFile = basePath + makeFileName

sourceFilePath = basePath + 'wLogA.log'
logAttendSave(sourceFilePath, makeFile)

sourceFilePath = basePath + 'wLogS.log'
logStatus(sourceFilePath, makeFile)

# csv 파일명
logFileName = 'wlog_'

# 코드별 csv 파일 분리 작업
#logSplitConf(basePath, makeFileName, logFileName, '111', '222', '333')

# csv 파일 열어서 수작업( 엑셀 사용 상태 만들기 xlsx )

stopwatch.stop()

print("실행 시간 :", stopwatch.get_elapsed_seconds())
print("-" * 88)