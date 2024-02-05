from movies import movies
def func(name):
    for movie in movies:
        if name==movie["name"] and movie["imdb"]>5.5:
            return True
    return False
print(func(input()))