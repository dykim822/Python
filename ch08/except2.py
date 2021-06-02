try:
    print("정수를 입력하세요")
    x = int(input())
    y = 100 / x
    print(f"나눗셈 결과 : {y}")  # x=0일 때 예외처리 필요
except ZeroDivisionError as err:
    print(err)
except ValueError as err:
    print(err)