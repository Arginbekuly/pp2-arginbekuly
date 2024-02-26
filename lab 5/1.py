import re
txt=input()
def reer(txt):
    pattern=r"ab*"
    m=re.findall(pattern,txt)
    print(m)
reer(txt)