import os
cur_list = os.listdir("./") # 현재 폴더 ch09
top_list = os.listdir("../ch08") # 상위 폴더 중 ch08
print('현재 디렉토리 목록')
for i in cur_list:
    print(i)
for j in top_list:
    print(j)
print(os.stat('./'))