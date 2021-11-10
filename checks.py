def valid_int(string) -> bool:
    if_valid = False

    if string != "":
        if (string[0] == "+" or string[0] == "-"):
            string = string[1 :]

        if string[0] != "0" and len(string) > 1 and string.isdigit():
            if_valid = True
        elif len(string) == 1 and string.isdigit():
            if_valid = True

    return if_valid


def check_for_valid_input_and_retype_to_int(string) -> int:
    while not valid_int(string):
        string = input("{} - это не целое число, попробуйте еще раз: ".format(string))

    return int(string)


def valid_input(string) -> bool:
    if string != "":
        if string[0] == "+" or string[0] == "-":
            string = string[1 :]

        if string.isdigit():
            if string[0] != 0:
                return True
        elif string.find("e") + 1:
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