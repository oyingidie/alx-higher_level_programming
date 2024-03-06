#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string is not str:
        return (0)
    r_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = [r_num[x] for x in roman_string] + [0]
    result = 0
    for i in range(len(num) - 1):
        if num[i] >= num[i + 1]:
            result += num[i]
        else:
            result -= num[i]
    return (result)
