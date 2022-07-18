#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new = []
    try:
        for i in range(list_length):
            try:
                new.append(my_list_1[i] / my_list_2[i])
            except ZeroDivisionError:
                new.append(0)
                print("Division by 0")
            except TypeError:
                new.append(0)
                print("Wrong type")
            except IndexError:
                new.append(0)
                print("Out of range")
    finally:
        return (new)
