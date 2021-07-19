import pandas as pd
s = pd.Series([9904312,3448737,2890451, 2466052], index=['서울','부산','인천','대구'])
print(s[1], s['부산'])
print(s[[0, 3, 1]])
print(s[['서울','대구','부산']])
print(s[1:3])
print(s['부산':'대구']) # 콜론 뒤에 인덱스 번호가 아닌 문자인 경우은 뒤 데이터 포함
print(s.부산, s.대구) # .을 이용하여 객체의 속성처럼 사용 가능
print('서울' in s) # 포함 여부 확인
print('대전' in s)