import os
path = 'C:\\Users\\argyn\\Desktop\\pp2\\lab 5'
name = ['kydyrali', 'argynbekuly', 'aktobe', 'almaty']
with open(path, 'w', encoding='utf-8') as file:
    for i in name:
        file.write(i + '\n')
print(path)
