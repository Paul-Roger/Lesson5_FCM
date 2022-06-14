#Console File Manager
"""После запуска программы пользователь видит меню, состоящее из следующих пунктов:
- создать папку;
- удалить (файл/папку);
- копировать (файл/папку);
- просмотр содержимого рабочей директории;
- посмотреть только папки;
- посмотреть только файлы;
- просмотр информации об операционной системе;
- создатель программы;
- играть в викторину;
- мой банковский счет;
- смена рабочей директории (*необязательный пункт);
- выход.
"""
import os
import shutil
import sys
import myconto
import victory

menu_items = [("Cоздать папку", 1), ("Удалить (файл/папку)", 2), ("Копировать (файл/папку)", 3), ("Просмотр содержимого рабочей директории", 4), ("Посмотреть только папки", 5), ("Посмотреть только файлы", 6), ("Просмотр информации об операционной системе", 7), ("Создатель программы", 8), ("Играть в викторину", 9), ("Мой банковский счет", 10), ("Смена рабочей директории", 11), ("Выход", 12)]

while True:
    print()
    for point in menu_items:
        print(point[1], point[0])
    usr_str = input("\nВыберите функцию > ")
    if usr_str.lower() == "exit":
        break
    if not usr_str.isdigit():
        print("Используйте число соотвутствующего пункта меню!\n")
        continue
    usr_num = int(usr_str)
    if usr_num == 12: # Выход
        print("Astalavista, baby!")
        break
    if usr_num == 1:  #создать папку
        usr_str = input("Введите имя новой папки: ")
        if not usr_str.isalnum():
            print("Ошибка - Недопустимое имя для папки")
        elif os.path.exists(usr_str):
                print("Папка с таким именем уже существует:")
        else:
            os.mkdir(usr_str)
    elif usr_num == 2: #удалить(файл / папку)
        usr_str = input("Введите имя новой папки/файла для удаления: ")
        if os.path.isfile(usr_str):
            os.remove(usr_str)  # remove the file
        elif os.path.isdir(usr_str):
            os.rmdir(usr_str) # remove dir
        else:
            print(f"В текущем каталоге нет папки или файла с именем {usr_str}")
    elif usr_num == 3: #копировать(файл / папку)
        src_str = input("Введите имя файла для копирования: ")
        if os.path.isfile(src_str):
            dst_str = input("введите путь/имя копии: ")
            shutil.copyfile(src_str, dst_str)
        else:
            print(f"В текущем каталоге нет файла с именем {src_str}")
    elif usr_num == 4:
        #просмотр содержимого рабочей директории
        print("Список файлов и папок в текущем каталоге:")
        with os.scandir(".") as entries:
            for entry in entries:
                print(entry.name)
    elif usr_num == 5:
        #посмотреть только папки
        print("Список папок в текущем каталоге:")
        with os.scandir(".") as entries:
            for entry in entries:
                if entry.is_dir():
                    print(entry.name)
    elif usr_num == 6:
        #посмотреть только файлы
        print("Список файлов в текущем каталоге:")
        with os.scandir(".") as entries:
            for entry in entries:
                if entry.is_file():
                    print(entry.name)
    elif usr_num == 7:
        #просмотр информации об операционной системе
        print(sys.platform)
    elif usr_num == 8:
        print("Programmed by Pavel Murashkin 12.06.2022\n")
    elif usr_num == 9:
        #играть в викторину
        victory.victory()
    elif usr_num == 10:
        #мой банковский счет
        myconto.conto()
    elif usr_num == 11:
        #смена рабочей директории
        print(f"текущий каталог - {os.getcwd()}")
        usr_str = input("Введите новый рабочий каталог: ")
        if os.path.exists(usr_str):
            os.chdir(usr_str)
        else:
            print("Такой каталог не найден")
    else:
        print("Такой пункт меню не существует!\n")