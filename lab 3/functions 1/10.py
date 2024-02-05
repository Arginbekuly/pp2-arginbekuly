a=[]
for i in range(int(input())):
    a.append(int(input()))
unique=[]
def Unique(a):
    for number in a:
        if number in unique:
            continue
        else:
            unique.append(number)
Unique(a)
print(unique)
