# recursive function
def f1(count):
    if count > 0:
        print(count, '현재')
        f1(count - 1)   # 조건을 변경하지 않으면 무한 loop
    print("결과", count)
f1(6)

# f1(6), f(5), ... , f(0) -> 결과0, 이전에 출력못한 (결과,count)를 최근 것들부터 출력한다
# 결과0, 결과1, 결과2, 결과3, 결과4, 결과5, 결과6 순서로 출력된다!