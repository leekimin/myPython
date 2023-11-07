from defUtils import logStatus, logAttendSave


""" example test.txt
2023-11-05 00:02:22.123 parameter:[ [IO -> (I), SESS_SEQ -> (788)]], header : {Wdd_Ses_UID=01097020365, Wdd_Ses_Key=20231104235817C3b1275ff3ea3410b91260e45e28df7c5, Wdd_Ses_ParticipantSEQ=119699, Wdd_Ses_PersonNm=, Wdd_Ses_SympSEQ=809}
2023-11-05 00:02:22.795 parameter:[], header : {Wdd_Ses_UID=01085949275, Wdd_Ses_Key=20231104235507Cc245b39a9b6d465b8e4b0406652ed325, Wdd_Ses_ParticipantSEQ=119794, Wdd_Ses_PersonNm=, Wdd_Ses_SympSEQ=809} 
2023-11-05 00:02:22.123 parameter:[ [IO -> (I), SESS_SEQ -> (801)]], header : {Wdd_Ses_UID=01097020365, Wdd_Ses_Key=20231104235817C3b1275ff3ea3410b91260e45e28df7c5, Wdd_Ses_ParticipantSEQ=119699, Wdd_Ses_PersonNm=, Wdd_Ses_SympSEQ=809}
2023-11-05 00:00:09.776 [ INFO] [http-nio-8084-exec-710] [SimpleLogApp.[32mbeforeParameterLog[0;39m:77] == methodName:wdd_AttendSave, parameter:[ [wdd_Prms -> ({"SESS_SEQ":788,"InYN":"Y"})]], header : {Wdd_Ses_UID=01047372571, Wdd_Ses_Key=20231104235852C6e50ace760114e249fe071877149107f, Wdd_Ses_ParticipantSEQ=119571, Wdd_Ses_PersonNm=, Wdd_Ses_SympSEQ=809}
"""

# status 체크용
logStatus('D:\\_my\\1105_conf\\test.txt', 'D:\\_my\\1105_conf\\testResult.txt')

logAttendSave('D:\\_my\\1105_conf\\test.txt', 'D:\\_my\\1105_conf\\testResult.txt')