#!/usr/bin/env python3
def no_c(my_string):
    string_list = list(my_string)
    index_counter = 0
    for index in string_list:
        if index == "c" or index == "C":
            string_list[index_counter] = ""
        index_counter = index_counter + 1
    return "".join(my_string_list)
