#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == "":
        return None
    big_num = 0
    for num in my_list:
        if num > big_num:
            big_num = num
    return big_num
