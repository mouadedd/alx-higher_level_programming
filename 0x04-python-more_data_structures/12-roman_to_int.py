#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    roman_dict = {'I': 1, 'V': 5, 'X': 10,'L': 50,
                  'C': 100, 'D': 500, 'M': 1000}
    decs = [roman_dict[i] for i in roman_string]
    res = 0
    for e in range(len(decs)):
        res += decs[e]
        if decs[e - 1] < decs[e] and e != 0:
            res -= (decs[e - 1] + decs[e - 1])
    return res
