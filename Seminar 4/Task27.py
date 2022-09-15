# 27. Строка содержит набор чисел. Показать большее и меньшее число Символ-разделитель - пробел
st= '34 65 23 7 5 3 3 4'

def convert_to_int(str):
    return [int(x) for x in str.split()]

str_list = convert_to_int(st)
print(min(str_list), max(str_list))