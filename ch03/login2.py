print("아이디를 입력하세요")
id = input()
print("비밀번호를 입력하세요")
password = input()
if id == 'root':
    if password == 'system':
        print("로그인 성공")
    else:
        print("비밀번호가 일치하지 않습니다")
else:
    print("존재하지 않는 ID입니다")