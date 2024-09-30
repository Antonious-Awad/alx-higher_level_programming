#!/usr/bin/python3
def safe_print_division(a, b):
    res = None
    try:
        res = a/b

    except ZeroDivisionError:
        res = None
    finally:
        print("Inside result: {:d}", res)
    return res
