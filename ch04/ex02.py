s = "user/local/bin/python"
# 경로 : "user/local/bin, 파일명: python
# rfind; reverse find 뒤에서부터 찾았을 때 처음으로 발견한 문자의 인덱스값
index = s.rfind("/")
print("경로 :", s[:index])
print("파일명 :", s[index+1:])