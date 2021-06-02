try:
    print("정수를 입력하세요")
    x = int(input())
    y = 100 / x
    print(f"나눗셈 결과 : {y}")  # x=0일 때 예외처리 필요
except ZeroDivisionError as err:
    print(err)
except ValueError as err:
    print(err)
else:
    print("Good Result!")
finally:    # 에러 여부와 관계없이 실행
    print("무조건 실행!")