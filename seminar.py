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
# d = int((float(input())*10) % 10)
# print(d)


# print('5. Дано число. Проверить кратно ли оно 5 и 10 или 15 но не 30:')


# def is_multiple(x, y):
#     if x != 0 and (y % x) == 0:
#         print(f"{y} кратное {x}")
#     else:
#         print(f"{y} не кратное {x}")


# x = int(input())
# list = [5, 10, 15, 30]
# for l in list:
#     is_multiple(x, l)


# print('6. Дано число обозначающее день недели. Вывести его название и указать является ли он выходным:')


# def getWeekDate(day):
#     days = ["Рождение дня недели =)", "Понедельник", "Вторник",
#             "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
#     return days[day]


# day = int(input('Укажите день недели цыфрой: '))
# week = getWeekDate(day)
# if (week == "Суббота" or week == "Воскресенье"):
#     print(f'День недели {week} -  выходной')
# else:
#     print(f'День недели {week}')


# print('7. Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат:')


# def logical_statement(x, y, z):
#     print(f"¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z} is {(not (x or y or z)) == (not x and not y and not z)}")
#     return (not (x or y or z)) == (not x and not y and not z)


# if (logical_statement(0, 0, 0) and logical_statement(0, 0, 1) and logical_statement(0, 1, 0) and
#     logical_statement(0, 1, 1) and logical_statement(1, 0, 0) and logical_statement(1, 0, 1) and
#         logical_statement(1, 1, 0) and logical_statement(1, 1, 1)):
#     print("Истинно")
# else:
#     print("Ложно")


# print('8. Сообщить в какой четверти координатной плоскости или на какой оси находится точка с координатами Х и У:')

# x = int(input("x="))
# y = int(input("y="))
# if x > 0 and y > 0:
#     print('I')
# elif x < 0 and y > 0:
#     print('II')
# elif x < 0 and y < 0:
#     print('III')
# elif x > 0 and y < 0:
#     print('IV')

# print('9. Указав номер четверти прямоугольной системы координат, показать допустимые значения координат для точек этой четверти:')

# number = int(input("Введите номер четверти (от 1 до 4): "))
# if number == 1:
#     print(f"Допустимые значения для {number} четверти: x > 0, y > 0")
# elif number == 2:
#     print(f"Допустимые значения для {number} четверти: x < 0, y > 0")
# elif number == 3:
#     print(f"Допустимые значения для {number} четверти: x < 0, y < 0")
# elif number == 4:
#     print(f"Допустимые значения для {number} четверти: x > 0, y < 0")
# else:
#     print("Неправильно ввели номер четверти прямоугольной системы координат!")


# print('10. Найти расстояние между двумя точками пространства:')

# firstPoint = list(map(int, input(
#     "Введите координаты первой точки x y z через пробел (например:  2 3 4):").split()))
# secondPoint = list(map(int, input(
#     "Введите координаты второй точки x y z через пробел (например:  2 3 4):").split()))
# result = (((secondPoint[0] - firstPoint[0])**2) + ((secondPoint[1] -
#           firstPoint[1])**2) + ((secondPoint[2] - firstPoint[2])**2))**(1/2)
# print(f"Расстояние между двумя точками пространства = {round(result, 2)}")

#########################################################################################################
print('1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр:')

number = input("Введите вещественное число: ")


def sum_number(numb):
    sum = 0
    for a in numb:
        sum += int(a)
    return sum


print(f"{number} ->", sum_number(number))
