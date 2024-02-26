import re
txt=input()
def stend(txt):
    pattern=r"a.*b$"
    m=re.findall(pattern,txt)
    print(m)
stend(txt)
