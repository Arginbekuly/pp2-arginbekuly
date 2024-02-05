class Myclass:
    def __init__(self):
        pass
    def getString(self):
        self.str=input()
    def printString(self):
        print(self.str.upper())

p1=Myclass()
p1.getString()
p1.printString