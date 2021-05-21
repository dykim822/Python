# fractions의 패키지에서 Fraction이라는 클래스를 갖고 와서 사용
# Fraction은 분수를 사용
from fractions import Fraction
# Fraction 2가지 형태로 사용할 수 있다
a1 = Fraction(5, 7) + Fraction('2/7')
print('a1 = ', a1)