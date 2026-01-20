#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    lst = []
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except (ZeroDivisionError, TypeError):
            result = 0
        except IndexError:
            result = 0
        lst.append(result)
    return lst
