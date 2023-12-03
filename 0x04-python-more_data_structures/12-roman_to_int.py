#!/usr/bin/env python3
def roman_to_int(roman_string):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                  'C': 100, 'D': 500, 'M': 1000}
    nums = []
    chif = int()

    if not roman_string or type(roman_string) is not str:
        return 0
    else:
        for i in roman_string:
            nums.append(roman_dict[i])

        for n in nums:
            if len(nums) == 1:
                chif = n
            elif nums[-1] < nums[0]:
                chif += n
            elif nums[-1] > nums[0]:
                s = sum(nums[:-1])
                chif = nums[-1] - s
        return chif
