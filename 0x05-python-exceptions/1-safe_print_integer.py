#!/usr/bin/python3
def safe_print_integer(value):
    try:
        #isinstance(value, int)
        print("{:d}".format(value))
    except (ValueError, TypeError):
        return False
    return True
