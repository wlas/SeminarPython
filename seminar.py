# print('1. По двум заданным числам проверить является ли одно квадратом второго:')
# print('Введите первое число')
# a = int(input('a = '))
# print('Введите второе число')
# b = int(input('b = '))
# if a*a != b and b*b != a:
#     print('не является квадратом')
# else:
#     print('является квадратом')


# print('2. Найти максимальное из пяти чисел:')
# print('Введите 5 чисел через пробел')
# numbers = input().split()
# maxNumb = 0

# for n in numbers:
#     if int(n) > maxNumb:
#         maxNumb = int(n)

# print(f'Mаксимальное из пяти введенных чисел: {maxNumb}')


print('3. Вывести на экран числа от -N до N:')
print('Введите первое отрицательное число')
a = int(input('a = '))
print('Введите второе положительное число')
b = int(input('b = '))

while a != b:
    print(a)
    a += 1