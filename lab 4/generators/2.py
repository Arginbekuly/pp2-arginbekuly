def get_even(n):
    for i in range(0,n+1):
        if i%2==0:
            yield i
n=int(input())
evens=get_even(n)
for i in evens:
    print(i,sep=",")