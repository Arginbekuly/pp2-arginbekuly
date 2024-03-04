import os
path = 'C:\\Users\\argyn\\Desktop\\pp2\\lab 5'
if os.path.exists(path):
    print("exist")
    print(os.path.basename)
    print(os.path.dirname)
else:
    print("not exists")