#автор: Есин Денис, ИУ7-16Б


#функция для инициализации списка через клавиатуру
def delete_and_make(array) -> None:
    #очищаем список
    array.clear()

    #вводим список
    array = input("Введите новый список через пробел: ").split()


#функция для вставки числа в список
def insert_into(array) -> None:
    #узнаем элемент и проверяем его валидность
    elem = input("Что надо вставить? ")

    #узнаем и проверяем индекс
    index = input("Куда? ")
    while not valid_int(index):
        index = input("Это не число, try again: ")
    index = int(index) - 1

    #вставляем элемент
    array.append(None)
    for i in range(len(array) - 1, index, -1):
        array[i] = array[i - 1]
    array[index] = elem


#функция для удаления элемента
def delete_element(array) -> None:
    #узнаем и проверяем номер элемента, который нужно удалить
    index = input("Какой элемент удалить? ")
    while not valid_int(index):
        index = input("Это не целое число, попробуйте еще раз:")
    index = int(index) - 1

    #проверяем, не вышел ли индекс за пределы списка
    #если нет, то удаляем элемент
    if -len(array) <= index < len(array):
        for i in range(index, len(array) - 1):
            array[i] = array[i + 1]
        del array[-1]
    else:
        print("Неверный индекс (вышел за границы списка)")


#функция для очистки списка
def clear(array) -> None:
    array.clear()


#функция для замены всех заглавных согласных английских букв на строчные
def uppercase_to_lowercase(array) -> list:
    #проходим по всем строкам в списке
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] in "BCDFGHJKLMNPQRSTVWXZ": #для каждой буквы в слове проверяем, заглавная согласная ли она
                array[i] = array[i].replace(array[i][j], array[i][j].lower()) #если да, то заменяем ее


#функция для поиска элемента с наибольшим числом английских согласных букв
def english_letters(array) -> str:
    max_quan = 0
    found_string = ""
    quan = 0
    for string in array:
        for letter in string:
            if letter.lower() in "bcdfghjklmnprstvwxz":
                quan += 1
        
        if max_quan < quan: 
            max_quan = quan
            found_string = string
        quan = 0

    return found_string


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
1 : Очистить список и ввести с клавиатуры
2 : Добавить элемент в список
3 : Удалить элемент по его номеру
4 : Очистить список
5 : Найти элемент с наибольшим числом английских согласных букв
6 : Замена всех заглавных согласных английских букв на строчные

Введите номер команды: """


#вводим команду и проверяем ее правильность
command = input(menu)
while not valid_int(command) or command not in ["0", "1", "2", "3", "4", "5", "6", "7"]:
    command = input("Введите корректный номер команды: ")


#и пока не введена команда выхода, продолжаем работу по кругу
while command != "0":
    #выполняем заданную команду
    if command == "1":
        delete_and_make()
        print("Ваш список: {}".format(array))
    elif command == "2":
        if array:
            insert_into()
            print("Ваш список: {}".format(array))
        else:
            print("Список еще не создан")
    elif command == "3":
        if array:
            delete_element()
            print("Ваш список: {}".format(array))
        else:
            print("Список еще не создан")
    elif command == "4":
        clear()
        print("Ваш список: {}".format(array))
    elif command == "5":
        if array:
            print("Строка с наибольшим количество англ. согл. букв: {}".format(english_letters()))
        else:
            print("Список еще не создан")
    elif command == "6":
        if array:
            uppercase_to_lowercase()
            print("Ваш список: {}".format(array))
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