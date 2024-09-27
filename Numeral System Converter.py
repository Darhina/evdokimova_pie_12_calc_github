# Программа для перевода чисел между различными системами счисления

# Функция перевода из одной системы счисления в другую
def convert_number(number, from_base, to_base):
    # Переводим исходное число в десятичную систему
    if from_base != 10:
        number = int(number, from_base)

    # Переводим десятичное число в целевую систему счисления
    if to_base == 2:
        return bin(number).replace("0b", "")
    elif to_base == 8:
        return oct(number).replace("0o", "")
    elif to_base == 16:
        return hex(number).replace("0x", "").upper()
    elif to_base == 10:
        return str(number)

