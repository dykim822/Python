class Shape:
    def draw(self):
        print("모형을 그린다")
class Triangle(Shape):
    def draw(self):
        print("삼각형을 그린다")
class Rectangle(Shape):
    def draw(self):
        print("사각형을 그린다")
class Circle(Shape):
    def draw(self):
        print("원을 그린다")
sh = [Triangle(), Rectangle(), Circle()]
for i in sh:
    i.draw()