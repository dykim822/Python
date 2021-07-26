import json
import pandas as pd
obj = { "name": "철수", "addr": "서울",
    "친척": [{"name": "길동", "age": 22 }, {"name": "나연","age": 17}] }
file = json.dumps(obj) # 파이썬 문장열로 변환
# print(file)
result = json.loads(file) # json 데이터로 해석
print(result)
sibings = pd.DataFrame(result['친척'], columns=['name','age'])
print(sibings)
a = pd.DataFrame(result)
print(a)
print(a.iloc[0, :2])
print(a.iloc[[0],[0,1]])