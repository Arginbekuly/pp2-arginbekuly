import re

def insert_spaces(text):
    pattern = r'(?<!^)(?=[A-Z])'
    result = re.sub(pattern, ' ', text)
    return result

text = input()
result = insert_spaces(text)
print(result)
