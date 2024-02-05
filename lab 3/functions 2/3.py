from movies import movies
def func(category):
    cate=[]
    for movie in movies:
        if category==movie["category"]:
            cate.append(movie["name"])
    return cate
print(func(input()))