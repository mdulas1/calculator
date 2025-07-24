'''
celebrities = " Davido-Wizkid-Rema-Portable-Buju-Burna"
print(celebrities)
names_of_celebrities = celebrities.split("-")
print(names_of_celebrities)
'''

message = "GhostNet#X44CR#98.654#TRC8821#Yes"
message_list = message.split("#")
print(message_list)

CodeName = message_list

print(f"CodeName:{CodeName[0]}")
MessageCode = message_list
print(f"messagecode: {MessageCode[1]}")

lastletter = message_list
print(f"lastlatter:{lastletter[1][-1]}")
TraceID = message_list
print(f"TraceID:{TraceID[3]}")

'''
CodeName: GhostNet
MessageCode: X44CR
lastletter: R
TraceID: TRC8821
Traceable: Yes
severitylevel: 98.65
'''
