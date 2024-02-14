def a_to_b(a,b):
    for i in range(a,b):
        yield i**2
a=int(input())
b=int(input())
square=a_to_b(a,b)
for i in square:
    print(i,end=" ")
