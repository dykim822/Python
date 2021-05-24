print("연도 4자리를 입력하세요")
year = int(input())
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    result = "윤년"
else:
    result = "평년"
print(f'입력한 {year}는 {result}입니다')