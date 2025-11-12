import pytest



@pytest.fixture(scope='module')
def create_list() -> list:
    """Создание списка с элементами"""
    data = [1,2,3,4,5,6,7,8,9,10]
    print('До выполнения yield')
    yield data  #Вывод наглядно показывает вывод печати, но по идеи scope='module' сделал тоже самое
    print('После выполнения yield')
#   После добавления scope='module' фикстура закрылась последней
#  SETUP    M create_list
#         test_fixtures.py::test_len_list (fixtures used: create_list).
#         SETUP    F create_dict
#         test_fixtures.py::test_len_dict (fixtures used: create_dict).
#         TEARDOWN F create_dict
#         SETUP    F create_tuple
#         test_fixtures.py::test_len_tuple (fixtures used: create_tuple).
#         TEARDOWN F create_tuple
#         test_fixtures.py::test_key_value (fixtures used: create_list).
#     TEARDOWN M create_list


@pytest.fixture()
def create_dict() -> dict:
    return {1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10}

@pytest.fixture()
def create_tuple() -> tuple:
    return (1,2,3,4,5,6,7,8,9,10)



def test_len_list(create_list):
    assert len(create_list) == 10
    assert type(create_list) == list

def test_len_dict(create_dict):
    assert len(create_dict) == 10
    assert type(create_dict) == dict

def test_len_tuple(create_tuple):
    assert len(create_tuple) == 10
    assert type(create_tuple) == tuple


def test_key_value(create_list):
    first = create_list[1]
    second = create_list[2]
    assert first != second


#  при выполнении команды `pytest --fixtures` вижу свои фикстуры