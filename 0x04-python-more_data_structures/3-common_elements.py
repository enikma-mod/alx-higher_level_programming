#!/usr/bin/python3
def common_elements(set_1, set_2):
    a_set = set(set_1)
    b_set = set(set_2)

    if (a_set & b_set):
        print(a_set & b_set)
    else:
        print("NO common elements")
