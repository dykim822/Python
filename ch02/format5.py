name = "홍길동"
print(f"안녕 {name:<10}님")
# 10칸을 확보해서 출력하는데 빈자리는 @로 채운다
print(f"안녕 {name:@<10}님")
print(f"안녕 {name:@>10}님")
print(f"안녕 {name:@^10}님")
pi = 3.1415923
print(f"파이 : {pi:0.2f}")