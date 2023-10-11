#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list and len(my_list):
        num = 0
        mem = 0
        for elem in my_list:
            num += (elem[0] * elem[1])
            mem += elem[1]
        return (num / mem)
    return 0
