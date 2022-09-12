# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

import random
lst = [random.randint(1,9) for i in range(5)]
print(f"Список: {lst}")

sum = 0
ls = []

for i in range(len(lst)):    
    if i % 2 != 0:
        ls.append(lst[i])
        sum += lst[i]

print(f"[{lst}] -> на нечётных позициях элементы {ls}, ответ: {sum}") 