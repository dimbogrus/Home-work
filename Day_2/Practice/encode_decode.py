"""
Задача №1
1.1 Написать программу, которая расшифрует строку.
Каждая символ - это две цифры. Отчет с 00 -> 'a', 01 -> 'b' и до 25 -> 'z',
26 - это пробел, он не входит в набор букв
Вход: строка из цифр. Выход: Текст.

1.2 Реализовать и расшифровку и зашифровку через функции
In/Out: '070411111426152419071413' <-> Out/In: 'hello python'

1.3 Добавить обработку неправильных входных данных.

1.4 Написать тесты для отработки корректных и некорректных данных.

"""

import string as st

st.ascii_lowercase


def sozdanie_dict() -> dict:
    translate_dict = {}
    for a in range(00, 26):
        if a < 10:
            translate_dict[f"0{a}"] = st.ascii_lowercase[a]
        else:
            translate_dict[f"{a}"] = st.ascii_lowercase[a]
    translate_dict[f"26"] = " "
    return translate_dict


def encode(sms: str) -> str:
    if not isinstance(sms, str):
        raise TypeError(f"Не правильный тип {type(sms)}")
    if len(sms) % 2 != 0:
        raise ValueError("Длина сообщения должна быть делима на 2 без остатка")
    shifr = sozdanie_dict()
    result = ""
    step_slice = 0
    for slice in range(2, len(sms) + 1, 2):
        number = sms[step_slice:slice]
        step_slice = slice
        result += shifr[number]
    return result


print(encode("070411111426152419071413"))


def decoder(sms: str) -> str:
    if not isinstance(sms, str):
        raise TypeError(f"Не правильный тип {type(sms)}")
    shifr = sozdanie_dict()
    result = ""
    for slice in sms:
        for k, v in shifr.items():
            if v == slice:
                result += k
    return result


print(decoder("hello python"))
