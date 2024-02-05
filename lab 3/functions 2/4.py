from movies import movies
def func():
    films=[]
    sum=0
    cnt=0
    for movie in movies:
        films.append(movie["name"])
        cnt+=1
    print("films:",films)
    for movie in movies:
        sum+=movie["imdb"]/cnt
    print("Average IMDB:",sum)
print(func())

