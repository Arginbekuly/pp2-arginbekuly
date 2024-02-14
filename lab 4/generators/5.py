def rev(n):
    for i in range(n,-1,-1):
        yield i
n=int(input())
num=rev(n)
for i in num:
    print(i,end=" ")