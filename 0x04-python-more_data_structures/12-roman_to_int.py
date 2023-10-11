#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    the_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
               'C': 100, 'D': 500, 'M': 1000}
    dictionary = [the_dict[i] for i in roman_string]
    res = 0
    for l in range(len(dictionary)):
        res += decs[l]
        if dictionary[l - 1] < dictionary[l] and l != 0:
            res -= (dictionary[l - 1] + dictionary[l - 1])
    return res
