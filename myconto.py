"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход

1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню

2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню

3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню

4. выход
выход из программы

При выполнении задания можно пользоваться любыми средствами

Для реализации основного меню можно использовать пример ниже или написать свой
"""

def str_to_num(line):
    #конвертирует строку в число
    line = line.strip()
    # если в строке только цифры
    if line.isdigit():
        return int(line)
    # если строка содержит точку или запятую
    elif (line.count('.')==1) ^ (line.count(',')==1):
        # если из строки убрать точку или запятую
        # и в строке останутся только цифры
        if any(line.replace(x, '').isdigit() for x in ['.', ',']):
            return float(line.replace(',', '.'))
    else:
        # ошибка
        print('Это не число!\n')
        return 0

def fill_acc(account):
    inp_str = input("Сумма пополнения: ")
    inp_num = str_to_num(inp_str)
    if inp_num > 0:
        print("успешно пополнили на " + str(inp_num))
        return account + inp_num
    else: return account

def buy(account, log):
    inp_str = input("Сумма покупки: ")
    inp_num = str_to_num(inp_str)
    if inp_num > 0:
        if inp_num <= account:
            inp_str = ''
            inp_str = input("Название товара: ")
            while (inp_str.strip() ==''):
                inp_str = input("Введите не пустое Название товара: ")
            account -=inp_num
            print("успешно купили " + inp_str + " за " + str(inp_num))
            log.append([inp_str, inp_num])
        else:
            print("Недостаточно средств для покупки!")
    else:
        print("Неверная сумма!")
    return account

def show_list(log):
    print("История покупок:")
    for i, p in log:
        print(i, p)

def conto():
    account = 0.0
    goods_list = list()

    while True:
        print('\n')
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход\n')

        choice = input('Выберите пункт меню: ')
        if choice == '1':
            account = fill_acc(account)
            print("текущий баланс " + str(account))
        elif choice == '2':
            account = buy(account, goods_list)
            print("текущий баланс " + str(account))
        elif choice == '3':
            show_list(goods_list)
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')
