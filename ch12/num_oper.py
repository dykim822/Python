import numpy as np
data = [0,1,2,3,4,5,6,7,8,9]
answer = []
# answer = data * 2
# print(answer)
for i in data:
    answer.append(i * 2)
print(answer)
arr1 = np.array(data)
print(2 * arr1)    # 한번에 처리가 가능