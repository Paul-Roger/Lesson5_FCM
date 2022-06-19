import math
import pytest
"""
2. В модуле написать тесты для встроенных функций filter, map, sorted, а также для функций из библиотеки math: pi, sqrt, pow, hypot. 
   Чем больше тестов на каждую функцию - тем лучше
"""

def test_filter():
    num_list = [0,1,2,3,4,5,6,7,8,9]
    assert list(filter(lambda x: x % 2 == 0, num_list))  == [0,2,4,6,8]
    name_list = ["Петр", "Анна", "Алексей", "Николай", "Леон", "Карина"]
    assert list(filter(lambda x: len(x) <= 4, name_list)) == ["Петр", "Анна", "Леон"]
    dict_list = [(1, "e"), (2, "d"), (3, "c"), (4, "b"), (5, "a")]
    assert list(filter(lambda x: x[0] <= 2, dict_list)) == [(1, "e"), (2, "d")]


def test_map():
    num_list = [0,1,2,3,4,5,6,7,8,9]
    assert list(map(lambda x: x*x , num_list))  == [0,1,4,9,16,25,36,49,64,81]
    name_list = ["Петр", "Анна", "Алексей", "Николай", "Леон", "Карина"]
    assert list(map(lambda x: x.upper(), name_list)) == ["ПЕТР", "АННА", "АЛЕКСЕЙ", "НИКОЛАЙ", "ЛЕОН", "КАРИНА"]

def test_sorted():
    num_list = [0,1,2,3,4,5,6,7,8,9]
    assert list(sorted(num_list, reverse=True))  == [9,8,7,6,5,4,3,2,1,0]
    name_list = ["Петр", "Анна", "Алексей", "Николай", "Леон", "Карина"]
    assert list(sorted(name_list, key = lambda x: len(x))) == ["Петр", "Анна",  "Леон", "Карина","Алексей", "Николай"]
    dict_list = [(1, "e"), (2, "d"), (3, "c"), (4, "b"), (5, "a")]
    assert list(sorted(dict_list, key = lambda x: x[1] )) == [(5, 'a'), (4, 'b'), (3, 'c'), (2, 'd'), (1, 'e')]

#===================================================================================================================
#math: pi, sqrt, pow, hypot
def test_pi():
    assert round(math.pi,2) == 3.14
    assert math.sqrt(16) == 4
    assert math.pow(2,10) == 1024
    assert math.hypot(3,4) == 5