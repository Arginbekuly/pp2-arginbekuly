import re
def posl(txt):
    pattern=r"abb*" or r"abbb*"
    m=re.findall(pattern , txt)
    print(m)
posl(input())