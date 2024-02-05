def spy_game(nums):
    k=0
    for i in nums:
        if k==0 and i==0:
            k+=1
        elif k==1 and i==0:
            k+=1
        elif k==2 and i==7:
            return True
    return False

        
print(spy_game([1,2,4,0,0,7,5])) 
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))    