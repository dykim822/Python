# Java의 Math class와 유사
import math
print(type(math.pi))     # 데이터형 확인할 때 type 사용
print("반지름이 {}인 원의 넓이은 {}입니다.".format(10, math.pi*10*10))
print("반지름이 "+str(10)+"인 원의 넓이은 "+str(math.pi*10*10)+"입니다.")
print("반지름이 ", str(10), "인 원의 넓이은 ", str(math.pi*10*10), "입니다.")
print("반지름이 %d인 원의 넓이은 %.2f입니다." %(10, math.pi*10*10))