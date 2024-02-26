import re

def camel_to_snake_case(camel_case_string):
    snake_case_string = re.sub(r'(?<!^)(?=[A-Z])', '_', camel_case_string).lower()
    return snake_case_string


camel_case_string =  input()
snake_case_string = camel_to_snake_case(camel_case_string)
print(snake_case_string)
