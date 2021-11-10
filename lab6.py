#автор: Есин Денис, ИУ7-16Б

#функция для инициализации списка элементами последовательности
def arr_initialization(n) -> None: 
    global array

    #проверка на валидность введенного х
    x = input("Введите х: ")
    while not valid_input(x):
        x = input("Это не число, try again: ")
    x = float(x)

    #если список ненулевой, очищаем его
    array.clear()

    #инициализируем список
    for i in range(1, n + 1):
        element = i * x / (2 ** i)
        array.append(element)


#функция для инициализации списка через клавиатуру
def delete_and_make() -> None:
    global array

    #очищаем список
    array.clear()

    #вводим список
    array = input("Введите новый список через пробел: ").split()

    #и проверяем каждый элемент,число ли это
    #если нет, то удаляем его
    for i in range(len(array)):
        if valid_input(array[i]):
            array[i] = float(array[i])
        else:
            print("{} элемент введен неправильно и будет удален".format(i))
            del array[i]


#функция для вставки числа в список
def insert_into() -> None:
    global array

    #узнаем элемент и проверяем его валидность
    elem = input("Что надо вставить? ")
    while not valid_input(elem):
        elem = input("Это не число, try again: ")
    elem = float(elem)

    #узнаем и проверяем индекс
    index = input("Куда? ")
    while not valid_input(index):
        index = input("Это не число, try again: ")
    index = int(index)

    #вставляем элемент
    array.insert(index, elem)


#функция для удаления элемента
def delete_element() -> None:
    global array

    #узнаем и проверяем номер элемента, который нужно удалить
    index = input("Какой элемент удалить? ")
    while not valid_int(index):
        index = input("Это не целое число, попробуйте еще раз:")
    index = int(index)

    #проверяем, не вышел ли индекс за пределы списка
    #если нет, то удаляем элемент
    if -len(array) <= index < len(array):
        del array[index]
    else:
        print("Неверный индекс (вышел за границы списка)")


#функция для очистки списка
def clear() -> None:
    global array

    array.clear()


#функция для нахождения экстремума
def extremum() -> int:
    global array

    #узнаем и проверяем номер экстремума
    number = input("Введите номер экстремума: ")
    while not valid_int(number):
        number = input("Вы ввели не целое число, попробуйте еще раз: ")
    number = int(number)

    #теперь пытаемся найти этот экстремум
    #если его нет, то просто проходится весь список
    quantity = 0
    i = 0
    while i < len(array) - 2 and quantity != number:
        i += 1
        if array[i - 1] > array[i] < array[i + 1] or array[i - 1] < array[i] > array[i + 1]:
            quantity += 1
    
    return quantity, number, i


#функция для поиска наиболее длнной последовательности
def sequence() -> list:
    global array

    temp_seq = [array[0]]
    max_seq = []

    for i in range(len(array) - 1):
        if array[i] * array[i + 1] < 0 and array[i] % 2 == 0 == array[i + 1] % 2:
            temp_seq += array[i]
        else:
            if len(max_seq) < len(temp_seq):
                max_seq = temp_seq
            temp_seq = [array[i]]

    return max_seq


#функция для проверки корректности ввода
def valid_input(string) -> bool:
    if string != "": #если строка вообще не пустая
        if string[0] == "+" or string[0] == "-": #убираем знак, если есть
            string = string[1 :]

        if string.isdigit(): #если остались только цифры
            if string[0] != 0:
                return True
        elif string.find("e") + 1: #если нашлось е, то проверяем корректность ввода с ним
            index = string.find("e")
            part_before = string[: index]
            part_after = string[index + 1 :]

            if part_after[0] == "-" or part_after[0] == "+":
                part_after = part_after[1 :]

            if part_before.find(".") + 1:
                index = part_before.find(".")
                
                if index == len(part_before) - 1: #
                    part_before = part_before[: len(part_before) - 1]
                elif index == 0:
                    part_before = part_before[1 :]
                else:
                    part_before = part_before[: index] + part_before[index + 1 :]

            if part_after.isdigit() and part_before.isdigit():
                return True
        elif string.find(".") + 1:
            index = string.find(".")
            string = string[: index] + string[index + 1 :]

            if string.isdigit():
                return True

    #если пройдна какая-то првоерка, то программа вернет True
    #а если нет, то дойдет досюда и вернет False
    return False


#функция проверки, введено ли целое число или нет
def valid_int(string) -> bool:
    if string != "":
        if (string[0] == "+" or string[0] == "-"):
            string = string[1 :]

        if string[0] != "0" and string.isdigit():
            return True
    return False


array = [] #сам список


#меню программы, которое выводится каждый раз после заврешения очередной комманды
menu = """0 : Выйти из программы
1 : Проинициализировать список элементами последовательности
2 : Очистить список и ввести с клавиатуры
3 : Добавить элемент в список
4 : Удалить элемент
5 : Очистить список
6 : Найти значение К-того экстремума
7 : Найти последовательность

Введите номер команды: """


#вводим команду и проверяем ее правильность
command = input(menu)
while not valid_int(command) or command not in ["0", "1", "2", "3", "4", "5", "6", "7"]:
    command = input("Введите корректный номер команды: ")


#и пока не введена команда выхода, продолжаем работу по кругу
while command != "0":
    #выполняем заданную команду
    if command == "1":
        n = input("Введите количество элементов: ")
        while not valid_int(n):
            n = input("Требуется ЦЕЛОЕ число: ")
        n = int(n)

        arr_initialization(n)
        print("Получившийся список: {}".format(array))
    elif command == "2":
        delete_and_make()
        print("Ваш список: {}".format(array))
    elif command == "3":
        if array:
            insert_into()
            print("Ваш список: {}".format(array))
        else:
            print("Список еще не создан")
    elif command == "4":
        if array:
            delete_element()
            print("Ваш список: {}".format(array))
        else:
            print("Список еще не создан")
    elif command == "5":
        clear()
        print("Ваш список: {}".format(array))
    elif command == "6":
        if array:
            quantity, number, i = extremum()
            
            if quantity == number:
                print("{} экстремум в списке: {}".format(number, array[i]))
            else:
                print("Экстремумов в списке меньше")
        else:
            print("Список еще не создан")
    elif command == "7":
        if array:
            max_seq = sequence()
            print("Наибольшая последовательность: {}".format(max_seq))
        else:
            print("Список еще не создан")

    #и снова выводим меню
    print()
    command = input(menu)
    while not valid_int(command) and command not in "01234567":
        command = input("Введите корректный номер команды: ")
else: #иначе прощаемся
    print("Goodbye!")
    exit(0)