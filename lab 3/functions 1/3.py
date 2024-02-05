numheads =int(input())
numlegs=int(input())
def solve(numheads,numlegs):
    chiken_num=(numlegs-numheads*2)/2
    rabbit_num=numheads-chiken_num
    return chiken_num,rabbit_num
print("num of chikens and rabbits:",solve(numheads,numlegs))
