from movies import movies
def func(category):
    cnt=0
    sum=0
    films=[]
    for movie in movies:
        if category==movie["category"]:
            films.append(movie["name"])         
    print("films:",films)
    for movie in movies:
            if movie['category'] == category:
                sum += movie['imdb']
                cnt += 1

    print ("Average IMDB:",sum/cnt)
print(func(input()))
    
    
