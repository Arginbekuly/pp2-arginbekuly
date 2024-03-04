import os
path = 'C:\\Users\\argyn\\Desktop\\pp2\\lab 6\\files A_Z'

for i in range(26):
    filename = chr(ord('A') + i) + ".txt"
    with open(filename, 'w') as file:
        file.write(f"This is file {filename}\n")
    print(f"File {filename} created.")