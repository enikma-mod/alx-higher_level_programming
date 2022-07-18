#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        total = fct(*args)
    except Exception as msg:
        total = None
        print("Exception: {}".format(str(msg)), file=sys.stderr)
    return total
