from defUtils import logStatus, logAttendSave, logSplitConf
from stopwatch import Stopwatch

print("-" * 88)

"""
logStatus('D:\\_my\\test.txt', 'D:\\_my\\testResult.txt')
logAttendSave('D:\\_my\\test.txt', 'D:\\_my\\testResult.txt')
"""

stopwatch = Stopwatch(2)
stopwatch.start()

# 파일하나로 머지
basePath = r'D:\\_my\\1105_conf\\20231203\\'

# 로그 취합할 하나의 로그 파일명
makeFileName = 'wLog_Total.csv'
makeFile = basePath + makeFileName

sourceFilePath = basePath + 'wLog_AttendSave.log'
logAttendSave(sourceFilePath, makeFile)

sourceFilePath = basePath + 'wLog_Status.log'
logStatus(sourceFilePath, makeFile)

# csv 파일명
logFileName = 'wlog_'

# 코드별 csv 파일 분리 작업
#logSplitConf(basePath, makeFileName, logFileName, '111', '222', '333')

# csv 파일 열어서 수작업( 엑셀 사용 상태 만들기 xlsx )

stopwatch.stop()

print("실행 시간 :", str(stopwatch))
print("-" * 88)