#      01234567890123
pin = "881120-1068234"
if pin[7] == '1':
    print("성별 : 2000년대 이전 남자")
elif pin[7] == '2':
    print("성별 : 2000년대 이전 여자")
elif pin[7] == '3':
    print("성별 : 2000년대 남자")
elif pin[7] == '4':
    print("성별 : 2000년대 여자")
else:
    print("외국인입니다")
print('=============================')
if int(pin[7]) == 1:
    print("성별 : 2000년대 이전 남자")
elif int(pin[7]) == 2:
    print("성별 : 2000년대 이전 여자")
elif int(pin[7]) == 3:
    print("성별 : 2000년대 남자")
elif int(pin[7]) == 4:
    print("성별 : 2000년대 여자")
else:
    print("외국인입니다")