# Создать массив случайных чисел в диапозоне (0, 20)

from random import randrange

a = [randrange(0, 21) for _ in range(7)]
print(a)
