from defUtils import logStatus, logAttendSave, logSplitConf

print("-" * 88)

"""
logStatus('D:\\_my\\1105_conf\\test.txt', 'D:\\_my\\1105_conf\\testResult.txt')
logAttendSave('D:\\_my\\1105_conf\\test.txt', 'D:\\_my\\1105_conf\\testResult.txt')
"""

# 파일하나로 머지
basePath = r'D:\\_my\\1105_conf\\20231119\\test\\'

# 로그 취합할 하나의 로그 파일명
makeFileName = 'wLog_Total.log'
makeFile = basePath + makeFileName

sourceFilePath = basePath + 'logAtt.log'
logAttendSave(sourceFilePath, makeFile)

sourceFilePath = basePath + 'logStatus.log'
logStatus(sourceFilePath, makeFile)

# csv 파일명
logFileName = 'wlog_'

# 코드별 csv 파일 분리 작업
logSplitConf(basePath, makeFileName, logFileName, '111', '222', '333')

# csv 파일 열어서 수작업( 엑셀 사용 상태 만들기 xlsx )

print("-" * 88)