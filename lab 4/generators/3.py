def by_three_four(n):
    for i in range(0,n+1):
        if i%3==0 and i%4==0:
            yield i
n=int(input())
by=by_three_four(n)
for i in by:
    print(i,end=" ")     

    