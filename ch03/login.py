print("아이디를 입력하세요")
id = input()
print("비밀번호를 입력하세요")
password = input()
if id == 'root' and password == 'system':   # python에서는 &&가 아닌 and사용
    print("로그인 성공")
elif id != 'root':
    print("존재하지 않는 ID입니다")
else:
    print("비밀번호가 일치하지 않습니다")