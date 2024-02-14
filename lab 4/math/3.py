import math
def area_reg(n,a):
    S=((n*(a**2)/4))*1/math.tan(math.pi/n)
    print(math.floor(S))
area_reg(int(input()),float(input()))