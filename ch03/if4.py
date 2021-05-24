print("정수를 입력하세요")
num = int(input())
if num % 2 == 0:
    result = "짝수"
else:
    result = "홀수"
print(f'입력한 {num}은 {result}입니다')