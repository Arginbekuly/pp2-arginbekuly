def func(grams):
    ounces = 0.03527396 * grams
    return ounces

grams = int(input())
print("in ounces =", func(grams))
