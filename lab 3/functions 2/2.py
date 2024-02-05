from movies import movies
def func():
    film=[]
    for movie in movies:
        if movie['imdb']>=5.5:
            film.append(movie['name'])
    return film
print(func())