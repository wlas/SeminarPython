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


# print('3. Вывести на экран числа от -N до N:')
# print('Введите первое отрицательное число')
# a = int(input('a = '))
# print('Введите второе положительное число')
# b = int(input('b = '))

# while a != b:
#     print(a)
#     a += 1



# print('4. Показать первую цифру дробной части числа:')
# print('Введите вещественное число через точку')
# d = int( (float(input())*10) % 10 )
# print(d)


print('5. Дано число. Проверить кратно ли оно 5 и 10 или 15 но не 30:')

def is_multiple(x,y):
    if x!=0 and (y%x)==0 :
       print(f"{y} кратное {x}")
    else:
       print(f"{y} не кратное {x}")

x = int(input())
list = [5, 10, 15, 30]
for l in list:
    is_multiple(x,l)