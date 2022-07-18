#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    n_list = [0] * list_length
    x = 0
    for i in range(list_length):
        try:
            x = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("Wrong type")
            x = 0
        except ZeroDivisionError:
            print("Division by 0")
            x = 0
        except IndexError:
            print("Out of range")
            x = 0
        finally:
            n_list[i] = x
    return (n_list)
