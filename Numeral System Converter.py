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


# Функция для отображения меню и получения данных от пользователя
def main():
    print("Программа для перевода чисел между системами счисления")
    print("1: Двоичная система счисления (2)")
    print("2: Восьмеричная система счисления (8)")
    print("3: Десятичная система счисления (10)")
    print("4: Шестнадцатеричная система счисления (16)")

    # Получаем исходную систему счисления
    from_base = int(input("Введите исходную систему счисления (2, 8, 10, 16): "))

    # Получаем целевую систему счисления
    to_base = int(input("Введите целевую систему счисления (2, 8, 10, 16): "))

    # Получаем число для перевода
    number = input(f"Введите число в системе счисления {from_base}: ")

    # Переводим число
    result = convert_number(number, from_base, to_base)

    # Выводим результат
    print(f"Результат перевода: {result}")
