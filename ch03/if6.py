print('정수를 입력하세요')
score = int(input())
if score > 60:
    message = '합격'
else:
    message = '불합격'
print(f"점수는 {score}점이고, 결과는 {message}입니다")

# python만 아래와 같이 사용 가능!
msg = "합격" if score >= 60 else "불합격"
print(f"점수는 {score}점이고, 결과는 {msg}입니다")