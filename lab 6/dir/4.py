import os
path = 'C:\\Users\\argyn\\Desktop\\pp2\\lab 6\\4.txt'
with open(path, 'r', encoding='utf-8') as file:
    str = sum(1 for x in file)
print(str)
