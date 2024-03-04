word = str(input())
def string(word):
    upper = 0
    lower = 0
    for char in word:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
    print(upper, lower)
string(word)