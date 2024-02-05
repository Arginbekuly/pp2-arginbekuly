mylist = []
for i in range(int(input())):
    mylist.append(int(input()))

def isPrime(mylist):
    cnt = 0
    for i in range(1, mylist+1):
        if mylist % i == 0:
            cnt += 1

    if cnt == 2: return True 
    else: return False   

primes=[]
def filter_prime(mylist):
    for j in mylist:
        if isPrime(j):
            primes.append(j)


filter_prime(mylist)
print(primes)