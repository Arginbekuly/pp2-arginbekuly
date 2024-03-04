def multiply(number):
    result = 1
    for i in number:
        result *= i
        
    return result
l = [1,3,4,5]
result = multiply(l)
print(result)