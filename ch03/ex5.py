a = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
sum = 0
for score in a:
    sum += score
print(f"평균 : {sum/len(a):.2f}")