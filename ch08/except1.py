try:
    print("정수를 입력하세요")
    x = int(input())
    y = 100 / x
    print(f"나눗셈 결과 : {y}")  # x=0일 때 예외처리 필요
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다")  # ZeroDivisionError, ValueError
except ValueError:
    print("정수가 아닙니다")