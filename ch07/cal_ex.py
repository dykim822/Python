import ch07.calculate
# from ch07.calculate import plus, multiply
from ch07.calculate import *    # *는 모두 사용가능, 메모리 소모로 권장x
import ch07.calculate as c
from ch07.calculate import multiply as m
# 1번 라인만 선언하면 아래와 같이 써야한다
print(ch07.calculate.plus(12, 6))
print(ch07.calculate.multiply(12, 6))

# 2번, 3번 라인처럼 선언하면 아래처럼 사용 가능
print(plus(1, 5))
print(multiply(2, 3))
print(divide(12, 5))

# 4번 라인처럼 선언하면 별칭으로 사용
print(c.minus(12, 5))
print(c.divide(12, 5))

# 5번 라인처럼 선언하면 별칭으로 사용 가능
print(m(3, 4))