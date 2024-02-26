import re
def upcase(txt):
    pattern="^([A-Z]{1}[a-z]*)*"
    m=re.findall(pattern,txt)
    print(m)
upcase(input())