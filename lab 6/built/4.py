import time
import math

def square_root(x):
    return math.sqrt(x)

def delayed_square_root(x, delay_ms):
    time.sleep(delay_ms / 1000)  # Переводим миллисекунды в секунды и создаем задержку
    result = square_root(x)
    return result

# Пример использования
number_to_sqrt = 25
delay_milliseconds = 1000  # Задержка в миллисекундах (1 секунда)

result = delayed_square_root(number_to_sqrt, delay_milliseconds)
print(f"Квадратный корень из {number_to_sqrt} после {delay_milliseconds / 1000} секунд: {result}")