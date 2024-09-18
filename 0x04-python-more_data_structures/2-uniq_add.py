#!/usr/bin/python3
def uniq_add(my_list=[]):
    set = set(my_list)
    sum = 0
    for i in set:
        sum += i
    return sum
