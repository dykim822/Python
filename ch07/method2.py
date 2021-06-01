class Counter:
    count = 0
    def __init__(self):
        Counter.count += 1
    @classmethod
    def print_count(cls):
        print(cls.count)    # cls사용하면 클래스 변수를 읽을 수 있다
c1 = Counter(); c2 = Counter(); c3 = Counter()
c3.print_count()
Counter.print_count()