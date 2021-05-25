# 총점과 평균을 구하라
score = [70, 60, 55, 90, 88, 76]
sum = 0
for sc in score:
    sum += sc
print(f"총점 : {sum}, 평균 : {sum / len(score)}")
print("총점 : {0}, 평균 : {1:.2f}".format(sum, sum/len(score)))
print(f"총점 : {sum}, 평균 : {sum / len(score):.2f}")