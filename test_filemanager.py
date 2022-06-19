import shutil
import os
import sys
import myconto

"""Тестируем функции из проекта Леонилдва Орлова"""

def filenames():
    result = []
    for item in os.listdir():
        if os.path.isfile(item):
            result.append(item)
    return result

def copy_file_or_directory(name, new_name):
    if os.path.isdir(name):
        shutil.copytree(name, new_name)
    else:
        shutil.copyfile(name, new_name)

#Тестируем не ЧИСТУЮ функцию:
def test_copy_file_or_directory():
    file_list = filenames()
    file_name = str(file_list[0])
    copy_file_or_directory(file_name,file_name+"01")
    file_list = filenames()
    assert file_name+"01" in file_list



def author_info():
    return 'Leonid Orlov'

#Тестируем ЧИСТУЮ функцию:
def test_author_info():
    assert author_info() == 'Leonid Orlov'


# соответствие месяца и его названия
months = {
    '01': 'января',
    '02': 'февраля',
    '06': 'июня'
}

# соответствие дня и его названия
days = {
    '01': 'первое',
    '02': 'второе',
    '03': 'третье',
    '04': 'четвертое',
    '12': 'двенадцатое',
    '26': 'двадцать шестое'
}

def date_to_str(date):
    """
    Функция приводит дату к текстовому виду
    :param date: дата в формате dd.mm.yyyy
    :return: дата в текстовом виде
    """
    day, month, year = date.split('.')
    result = f'{days[day]} {months[month]} {year} года'
    return result

def test_date_to_str():
    assert date_to_str("04.02.1799") == "четвертое февраля 1799 года"


def separator(count=30):
    """
    Функция разделитель
    :param count: количество звездочек
    :return: красивый разделитель
    """
    return '*' * count

#nтестируем простую функцию
def test_separator():
    assert separator(5) == "*****"
    assert separator() == 30*"*"

#естируем новыt функции дяя myconto
def test_myconto():
    myconto.save_acc(12.345, 'conto.bin')
    assert myconto.restore_acc('conto.bin') == 12.345

def test_log():
    myconto.save_log([["AAA", 12.34], ["BBB", 43.21]], 'purch.log')
    assert myconto.restore_log('purch.log') == [["AAA", 12.34], ["BBB", 43.21]]