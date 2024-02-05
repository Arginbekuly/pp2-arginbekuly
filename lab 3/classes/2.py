class Shape:
    def __init__(self, leng, wid):
        pass
    def area(self):
        return self.leng * self.wid


class Square(Shape):
    def __init__(self, leng=0):
        self.leng = leng
        self.wid = leng


p1 = Square(int(input()))
print(f"area of the square: {p1.area()}")