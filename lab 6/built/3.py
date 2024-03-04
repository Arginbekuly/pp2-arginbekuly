def is_palindrome(s):
    # Приводим строку к нижнему регистру и удаляем пробелы
    s = s.lower().replace(" ", "")
    
    # Сравниваем строку с её обратным порядком
    return s == s[::-1]

# Пример использования
input_string = input("Введите строку: ")
if is_palindrome(input_string):
    print("Это палиндром!")
else:
    print("Это не палиндром.")