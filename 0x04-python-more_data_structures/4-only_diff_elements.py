#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    print(set_1.difference(set_2))
    print(set_2.difference(set_1))

    # difference() returns the difference of two or more sets as a new set
    # return set_1 ^ set_2
