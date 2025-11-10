"""
Задача №1
Вход:
Пользователь должен ввести 'правильный' пароль, состоящий из:
цифр, букв латинского алфавита(строчные и прописные) и
специальных символов  special = '_!@#$%^&'.
Всего 4 набора различных символов.
В пароле обязательно должен быть хотя бы один символ из каждого набора.
Длина пароля от 8(мин) до 15(макс) символов включительно.
Максимальное количество попыток ввода неправильного пароля - 5.
Каждый раз выводим номер попытки.
Желательно выводить пояснение, почему пароль не принят и
что нужно исправить.

* Добавить проверку, что в пароле только символы из 4-х наборов.

Как вариант:
check_password('some string') -> tuple[bool, str]
(True, reasons)
(False, reasons)


Оформить решения в виде модуля

import string as st
st.digits
st.ascii_lowercase
st.ascii_uppercase
special = '_!@#$%^&'

Выход:
пароль подходит / не подходит

Пример:
пароль подходит -> o58anuahaunH!
пароль подходит -> aaaAAA111!!!
пароль не подходит -> saucacAusacu8
"""

import string as st

st.digits
st.ascii_lowercase
st.ascii_uppercase
special = "_!@#$%^&"


def check_password(password: str) -> tuple[bool, str]:
    dig = low = up = spec = False
    check_all = ""

    if 8 <= len(password) <= 15:
        for i in password:
            if i in st.digits:
                dig = True
            if i in st.ascii_lowercase:
                low = True
            if i in st.ascii_uppercase:
                up = True
            if i in special:
                spec = True
        if dig == low == up == spec == True:
            check = (True, "Пароль введен корректно")
        else:
            if not dig:
                check_all += "Не использовались цифры регистр\n"
            if not low:
                check_all += "Не использовался нижний регистр\n"
            if not up:
                check_all += "Не использовался верхний регистр\n"
            if not spec:
                check_all += 'Не использовался спецсимвол "_!@#$%^&"\n'
            check = (False, check_all)
    else:
        check = (False, "Длина пароля не соответсвуют условию")

    return check


def input_password():
    for schet in range(0, 5):
        password = input("Введите пароль: ")
        print(f"Попытка ввода пароля: {schet+1}")
        check, msg = check_password(password)
        print(msg)
        print("-" * 20)
        if check:
            break


if __name__ == "__main__":
    input_password()
