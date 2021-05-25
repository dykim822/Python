print("수박의 무게를 입력하세요")
weight = int(input())
if weight > 10:
    result = 1
elif weight > 7:
    result = 2
elif weight > 4:
    result = 3
else:
    result = 4
print(f"입력한 수박의 무게는 {weight} kg이고 {result}등급입니다")