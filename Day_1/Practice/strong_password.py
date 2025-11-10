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


def check_password(password: str) -> tuple:
    dig = False
    dig_text = "Не использовались цифры регистр"
    low = False
    low_text = "Не использовался нижний регистр"
    up = False
    up_text = "Не использовался верхний регистр"
    spec = False
    spec_text = 'Не использовался спецсимвол "_!@#$%^&"'

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
    check = (dig, dig_text, low, low_text, up, up_text, spec, spec_text)
    return check


def len_password():
    schet = 0
    try_password = True
    while try_password:
        if schet < 4:
            password = input("Введите пароль: ")
            schet += 1
            print(f"Попытка ввода пароля: {schet}")
            if 8 <= len(password) <= 15:
                result = check_password(password)
                if False in result:
                    print("Неудача")
                    print(result)
                else:
                    print("Пароль введен корректно")
                    try_password = False
            else:
                print("Неудача")
                print("Длина пароля не соответсвуют условию")
        else:
            try_password = False
        print("-" * 20)


if __name__ == "__main__":
    len_password()
