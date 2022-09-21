# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

str_text = "Одна девочка ушла из дома в лес абв. В лесу она заблуабвдилась и стала искать дороабвгу домой, да не нашла, а пришла в лесу к домабвику."

def del_words(str_text):
    str_text = list(filter(lambda x: 'абв' not in x, str_text.split()))
    return " ".join(str_text)

str_text = del_words(str_text)
print(str_text)