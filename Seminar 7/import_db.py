# модуль импорта данных
import user_interface as ui


def import_data(data, sep=None):
    with open('db.csv', 'a+') as file:
        if sep == None:
            for i in data:
                file.write(f"{i}\n")
            file.write(f"\n")
        else:
            file.write(sep.join(data))
            file.write(f"\n")


def input_data():
    last_name = ui.get_input_user("Укажите Фамилию")
    first_name = ui.get_input_user("Укажите Имя")
    phone_number = ui.get_input_user("Укажите Телефон")
    return [last_name, first_name, phone_number]


def choice_sep():
    sep = ui.get_input_user("Укажите разделитель(, ; :)")
    if sep == "":
        sep = None
    return sep
