import sys

gender = input("남/여 중에 하나를 입력하세요 : ")
cnt = int(input("팔굽혀펴기 횟수를 입력하세요 : "))
if gender == '남':
    if cnt > 10:
        grade = '합격'
    else:
        grade = '불합격'
elif gender == '여':
    if cnt >= 5:
        grade = '합격'
    else:
        grade = '불합격'
else:
    print('프로그램 종료')
    sys.exit(0)

print(f"성별은 {gender}자이고, 팔굽혀펴기 횟수는 {cnt}회이며, 등급은 {grade}입니다")