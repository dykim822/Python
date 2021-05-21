a = "Hello"
print(a.startswith("H"))    # H로 시작하는지 아닌지 true/false
print(a.endswith("o"))      # o로 끝나는지 아닌지
print(a.endswith("h"))      # f로 끝나는지 아닌지
print(a.find("l"))          # l문자의 인덱스 번호(개수x)
print(a.rfind("l"))         # 뒤부터 찾을 때 찾은 l은 인덱스 번호
print(a.count("l"))         # l의 갯수
b = "ABCdef"
print(b.isalpha())          # b가 알파벳인지?
print(b.isalnum())          # b가 알파벳 또는 숫자인지?
print(b.isnumeric())        # b가 숫자인지?
c = "Hello, World"
print(c.replace("Hello", "안녕하세요"))
print(c.split(','))         # 콤마를 기준으로 split/ 배열(list)로 변경
li = c.split(',')
print(li[0]);   print(li[1])
print(b.upper())            # b를 대문자로 변경
print(b.lower())            # b를 소문자로 변경