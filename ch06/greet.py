def hello_korean():
    print("안녕하세요")
def hello_english():
    print("Hello")
def greet(k):
    k()
def get_greet(k):
    if k == 'k':
        return hello_korean   # 함수 이름도 반환 가능
    else:
        return hello_english

# 함수를 매개변수로 사용해서 호출 가능
# 합성함수 같은 원리
greet(hello_korean)
greet(hello_english)

g = get_greet('k')
g()
g = get_greet('e')
g()