#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    the_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                'C': 100, 'D': 500, 'M': 1000}
    dictionary = [the_dict[i] for i in roman_string]
    res = 0
    for x in range(len(dictionary)):
        res += decs[x]
        if dictionary[x - 1] < dictionary[x] and x != 0:
            res -= (dictionary[x - 1] + dictionary[x - 1])
    return res
