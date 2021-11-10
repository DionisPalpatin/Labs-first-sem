#импорт модуля, содержашего функции для проверки вводимых строк
import checks

#функция создания матрицы
def creat_matrix(matrix):
    matrix.clean()

    #ввод количества столюцов в матрице и проверка, чтобы это было целое число
    matrix_width = input("Сколько cтолбцов в матрице? ")
    matrix_width = checks.check_for_valid_input_and_retype_to_int(matrix_width)

    #ввод количества строк в матрице и проверка, чтобы это было целое число
    matrix_height = input("Сколько строк в матрице? ")
    matrix_height = checks.check_for_valid_input_and_retype_to_int(matrix_height)

    #теперь вводим строки матрицы в строчку через пробел
    for i in range(matrix_height):
        matrix_row = input("Введите строку матрицы: ").split()

        #пока введенная строка не соответсвтует заявленной ширине матрицы, просим ввести строку еще рах
        while len(matrix_row) != matrix_width:
            matrix_row = input("Длина строки не соответствовала заявленной ранее, попробуйте снова: ").split()

        #проверяем каждое число, чтобы оно было целым числом
        for j in range(len(matrix_row)):
            matrix_row[j] = checks.check_for_valid_input_and_retype_to_int(matrix_row[j])

        #если все ок, добавляем строку в матрицу
        matrix.append(matrix_row)


#функция вставки строки в матрицу
def insert_row(matrix, algoritmic):
    new_row = input("Введите строку матрицы: ").split()
    while len(new_row) != len(matrix[0]):
            new_row = input("Длина строки не соответствует длине других строк, попробуйте снова: ").split()

    #проверка каждого числа в строке на корректность и его замена в случае неправильноси
    for j in range(len(new_row)):
        new_row[j] = checks.check_for_valid_input_and_retype_to_int(new_row[j])

    string_position_in_matrix = input("Введите номер этой строки: ")
    string_position_in_matrix = checks.check_for_valid_input_and_retype_to_int(string_position_in_matrix)

    #проверка корректности введенного номера строки
    while not (1 <= string_position_in_matrix <= len(matrix)):
        string_position_in_matrix = input("Пожалуйста, учтите, что номер строки лежит на отрезке от 1 до номера последней строки: ")
        string_position_in_matrix = checks.check_for_valid_input_and_retype_to_int(string_position_in_matrix)

    #выполнение с помощью встроенных функций или нет
    if algoritmic:
        matrix += [None]
        string_position_in_matrix -= 1

        for i in range(len(matrix) - 1, string_position_in_matrix, -1):
            matrix[i] = matrix[i - 1]
        matrix[string_position_in_matrix] = new_row
    else:
        matrix.insert(string_position_in_matrix, new_row)


#функция удаления строки
def delete_row(matrix, algoritmic):
    string_index_to_delete = input("Введите номер этой строки: ")
    string_index_to_delete = checks.check_for_valid_input_and_retype_to_int(string_index_to_delete)

    #проверка корректности введенного номера
    while not (1 <= string_index_to_delete <= len(matrix)):
        string_index_to_delete = input("Пожалуйста, учтите, что номер строки лежит на отрезке от 1 до номера последней строки: ")
        string_index_to_delete = checks.check_for_valid_input_and_retype_to_int(string_index_to_delete)

    string_index_to_delete -= 1

    #алгоритическое или с помощью встроенных функций выполнение
    if algoritmic:
        for i in range(string_index_to_delete, len(matrix) - 1):
            matrix[i] = matrix[i + 1]

        del matrix[-1]
    else:
        del matrix[string_index_to_delete]


#функция для вставки столбца
def insert_column(matrix, algoritmic):
    new_column = input("Введите столбец: ").split()
    #проверка соотвествия длинны столбца высоте матрицы
    while len(column) != len(matrix):
        column = input("Длина столбца не соответствует длине других столбцов, попробуйте снова: ")

    #проверка каждого введенного символа
    for i in range(len(new_column)):
        new_column[i] = checks.check_for_valid_input_and_retype_to_int(new_column[i])

    column_number_to_insert = input("Введите номер столбца: ")
    column_number_to_insert = checks.check_for_valid_input_and_retype_to_int(column_number_to_insert)

    while not (1 <= column_number_to_insert <= len(matrix[0])):
        column_number_to_insert = input("Пожалуйста, учтите, что номер столбца лежит на отрезке от 1 до номера последней столбца: ")
        column_number_to_insert = checks.check_for_valid_input_and_retype_to_int(column_number_to_insert)

    column_number_to_insert -= 1

    if algoritmic:
        for row in range(len(matrix)):
            matrix[row] += [None]

            for column in range(len(matrix[row]) - 1, column_number_to_insert, -1):
                matrix[row][column] = matrix[row][column - 1]

            matrix[row][column] = new_column[row]
    else:
        for row in range(len(matrix)):
            matrix[row].insert(column_number_to_insert, new_column[row])


def delete_column(matrix, algoritmic):
    column_index_to_delete = input("Введите номер этой строки: ")
    column_index_to_delete = checks.check_for_valid_input_and_retype_to_int(column_index_to_delete)

    while not (1 <= column_index_to_delete <= len(matrix)):
        column_index_to_delete = input("Пожалуйста, учтите, что номер строки лежит на отрезке от 1 до номера последней строки: ")
        column_index_to_delete = checks.check_for_valid_input_and_retype_to_int(column_index_to_delete)

    column_index_to_delete -= 1

    if algoritmic:
        for row in range(len(matrix)):
            for column in range(column_index_to_delete, len(row) - 1):
                matrix[row][column] = matrix[row][column + 1]

            del matrix[row][-1]
    else:
        for row in range(len(matrix)):
            del matrix[row][column_index_to_delete]


def maximum_number_of_identical_elements_in_row(matrix):
    row_to_find = None
    maximum_number_in_all_rows = 0 #запоминаем максимально число требуемых элементов в матрице

    for row in matrix:
        maximum_number_in_current_row = 0 #запоминаем максимально число требуемых элементов в каждой строке
        current_quan = 1 #и текущее число тех же элементов

        for column in range(1, len(row)):
            if row[column] == row[column - 1]:
                current_quan += 1
            else:
                maximum_number_in_current_row = max(current_quan, maximum_number_in_current_row)
                current_quan = 1
        
        if maximum_number_in_current_row > maximum_number_in_all_rows:
            maximum_number_in_all_rows = maximum_number_in_current_row
            row_to_find = row

    return maximum_number_in_all_rows, row_to_find


def swap_lines_with_max_and_min_numbers_of_negative_elements(matrix):
    index_of_min, index_of_max = -1, -1
    min_number, max_number = len(matrix[0]) + 1, 0

    for line in range(len(matrix)):
        counter = 0

        for element in matrix[line]:
            if element < 0: counter += 1

        if counter < min_number:
            index_of_min = line
            min_number = counter
        if counter > max_number:
            index_of_max = line
            max_number = counter

    matrix[index_of_max], matrix[index_of_min] = matrix[index_of_min], matrix[index_of_max]


def min_difference_between_two_summ(matrix):
    min_summ_in_the_whole_matrix = float("inf")
    index_of_column = None

    for column in range(len(matrix[0])):
        current_summ = 0

        for line in range(len(matrix)):
            current_summ += matrix[line][column]

        if min_difference_between_two_summ > abs(current_summ):
            min_difference_between_two_summ = abs(current_summ)
            index_of_column = line

    column_with_min_diff = []
    for line in matrix:
        column_with_min_diff.append(line[index_of_column])

    return min_summ_in_the_whole_matrix, column_with_min_diff, index_of_column


def swap_columns_with_min_and_max_summ_of_elements(matrix):
    max_summ, min_summ = float("-inf"), float("inf")
    index_max_summ, index_min_summ = -1, -1

    for column in range(len(matrix[0])):
        current_summ = 0

        for line in matrix:
            current_summ += line[column]

        if current_summ > max_summ:
            max_summ = current_summ
            index_max_summ = column
        if current_summ < min_summ:
            min_summ = current_summ
            index_min_summ = column

    for line in range(len(matrix)):
        matrix[line][index_min_summ], matrix[line][index_max_summ] = matrix[line][index_max_summ], matrix[line][index_min_summ]


def print_matrix(matrix):
    print("На данный момент матрица такая: ")

    for line in matrix:
        for elem in line:
            print("{:^5}".format(elem), end="")
        print("\n")


menu = """0 : Выйти из программы
1 : Ввести матрицу
2 : Добавить строку
3 : Удалить строку
4 : Добавить столбец
5 : Удалить столбец
6 : Найти строку с наибольим количеством идущих подряд одинаковых элементов
7 : Переставить местами строки с наибольшим и наимменьшим количеством
    отрицательных элементов
8 : Найти столбец, у которого разница между суммой положительных и
    отрицательных элементов минимальна
9 : Переставить местами столбцы с минимальной и максимальной суммами эл-тов
10 : Вывести матрицу
11 : Включить/выключить алгоритмическое выполнение пунктов 2-5"""


matrix = []
algoritmic = False


command = input("Введите номер команды: ")
command = checks.check_for_valid_input_and_retype_to_int(command)


while not (0 <= command <= 11):
    command = input("Неккорректный номер команды, попробуйте еще раз: ")
    command = checks.check_for_valid_input_and_retype_to_int(command)


while command:
    if command == 1:
        creat_matrix(matrix)
        print_matrix(matrix)
    elif command == 2:
        insert_row(matrix, algoritmic)
        print_matrix(matrix)
    elif command == 3:
        delete_row(matrix, algoritmic)
        print_matrix(matrix)
    elif command == 4:
        insert_column(matrix, algoritmic)
        print_matrix(matrix)
    elif command == 5:
        delete_column(matrix, algoritmic)
        print_matrix(matrix)
    elif command == 6:
        maximum, line = maximum_number_of_identical_elements_in_row(matrix)
        print("Макимальное число одинаковых элементов равно {} и нашлось в строке {}".format(maximum, line))
    elif command == 7:
        swap_lines_with_max_and_min_numbers_of_negative_elements(matrix)
        print_matrix(matrix)
    elif command == 8:
        min_summ, column, index = min_difference_between_two_summ(matrix)
        print("Минимальная разница равна {} и встречается в столбце {} (столбец {})".format(min_summ, column, index))
    elif command == 9:
        swap_columns_with_min_and_max_summ_of_elements(matrix)
        print_matrix(matrix)
    elif command == 10:
        print_matrix(matrix)
    else:
        mode = input("Включить или выключить? (напишите true/false): ")
        while "true" != mode.lower() != "false":
            mode = input("Неправильная команда, попробуйте еще раз: ")
        else:
            if mode.lower() == "true": 
                algoritmic = True
            else: 
                algoritmic = False
else:
    print("Goodbye!")
    exit()