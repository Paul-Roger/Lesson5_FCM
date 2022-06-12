import random
"""
(МОДУЛЬ 4) В проекте создать новый модуль victory.py. Задание
Написать или улучшить программу Викторина из предыдущего дз (Для тренировки предлагаю не пользоваться никакими библиотеками кроме random)
Есть 10 известных людей и их даты рождения в формате '02.01.1988' ('dd.mm.yyyy') - предлагаю для тренировки пока использовать строку
Программа выбирает из этих 10-и 5 случайных людей, это можно реализовать с помощью модуля random и функции sample
Пример использования sample:
import random
numbers = [1, 2, 3, 4, 5]

# 2 - количество случайных элементов
result = random.sample(numbers, 2)

print(result) # [5, 1]

После того как выбраны 5 случайных людей, предлагаем пользователю ввести их дату рождения
пользователь вводит дату в формате 'dd.mm.yyyy'

Например 03.01.2009, если пользователь ответил неверно, то выводим правильный ответ, но уже в следующем виде: третье января 2009 года, склонением можно пренебречь

В конце считаем количество правильных и неправильных ответов и предлагаем начать снова
"""
def victory():
    famous_name = ("А.С.Пушкин","М.Ю.Лермонтов","И.С.Тургенев","Л.Н.Толстой","И.А.Бунин","Н.А.Некрасов","Н.В.Гоголь","А.Н.Островский","М.А.Булгаков","М.Е.Салтыков-Щедрин")
    famous_date = ("26.05.1799", "15.10.1814", "9.11.1818", "9.09.1828", "22.10.1870", "10.12.1821", "1.04.1809", "12.04.1823", "15.05.1891", "27.01.1826")
    months = ("января", "февраля", "марта", "апреля", "мая", "июня", "июля", "августа", "сентября", "октября", "ноября", "декабря")
    days = ("первое", "втоорое", "третье", "четвертое", "пятое", "шестое", "седьмое", "восьмое", "девятое", "демятое", "одиннадцатое",
        "двеннадцатое", "тринадцатое", "четырнадцатое" , "пятнадцатое" , "шестнадцатое" , "семнадцатое" , "воемнадцатое" ,"девятнадцатое" , "двадцатое" ,
        "двадцать первое" , "двадцать второе" , "двадцать третье" , "двадцать четвертое" , "двадцать пятое" , "двадцать шестое" , "двадцать седьмое" , "двадцать восьмое" , "двадцать девятое" , "тридцатое" , "тридцать первое")

    while True:
        i = 0
        points = 0
        exit_code = 0

        q_nums =[]
        for i in range(5):
            rnd_int = random.randint(0, 9)         #generate new int
            while rnd_int in q_nums:                #check if unic
                rnd_int = random.randint(0, 9)
            q_nums.append(rnd_int)

        print("укажите год рождения следующеих авторов:")
        for i in q_nums:
            while True:
                user_input = input(famous_name[i] + "> ")
                date_str = user_input.replace("/",".").replace("-",".").replace(",",".")
                user_list = date_str.split(".")
                if len(user_list) == 3:
                    if not user_list[0].isdigit() or not user_list[0].isdigit() or not user_list[0].isdigit():
                        print("неверный формат даты")
                    else:
                        break
                else:
                    print("неверный формат даты")
            answer_str = famous_date[i]
            answer_list = answer_str.split(".")
            date_matches = True
            for i in range(len(answer_list)):
                if user_list[i].isdigit():
                    date_matches &= (int(answer_list[i]) == int(user_list[i]))
                else:
                    date_matches = False
            if date_matches:
                points += 1
            else:
                print(int(answer_list[1]))
                print("неверно! правильный ответ ", days[int(answer_list[0])-1], months[int(answer_list[1])-1], answer_list[2])
        print("правильных ответов:   " + str(points) + " - " + str(points * 100 / 5) + " %")
        print("неправильных ответов: " + str(5 - points) + " - " + str((5 - points) * 100 / 5) + " %")
        while True:
            user_input = input("Хотите начать заново (да/нет)? ")
            if  user_input == "нет" or user_input == "Нет" or user_input == "НЕТ":
                exit_code = 0
                break
            elif  user_input == "да" or user_input == "Да" or user_input == "ДА":
                exit_code = 1
                break
            else:
                exit_code = 9
        if exit_code == 0:
            break

