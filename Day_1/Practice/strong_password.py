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
    dig_text = "Не использовались цифры регистр"
    low_text = "Не использовался нижний регистр"
    up_text = "Не использовался верхний регистр"
    spec_text = 'Не использовался спецсимвол "_!@#$%^&"'

    if 8 <= len(password) <= 15:
        for i in password:
            if i in st.digits:
                dig = True
                dig_text = "Цифры использовались"
            if i in st.ascii_lowercase:
                low = True
                low_text = "Использовался нижний регистр"
            if i in st.ascii_uppercase:
                up = True
                up_text = "Использовался верхний регистр"
            if i in special:
                spec = True
                spec_text = 'Использовался спецсимвол "_!@#$%^&"'
        check_all = (
            dig,
            dig_text,
            low,
            low_text,
            up,
            up_text,
            spec,
            spec_text,
        )

        if all(check_all):
            check = (True, "Пароль введен корректно")
        print("Неудача")
        print(check_all)
        check = (False, "Условия не соблюдены, смотри лог")
    else:
        print("Неудача")
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
