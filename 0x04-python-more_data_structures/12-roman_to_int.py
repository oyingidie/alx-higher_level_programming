#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string == None or type(roman_string) != str:
        r_num = {
                'I': 1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000
                }
        result = 0
        i = 0
        while i < len(roman_string):
            c_char = roman_string[i]
            c_value = r_num.get(c_char)
        if not value:
            return (0)
        if i + 1 < len(roman_string) and c_value < r_num.get(roman_string[i + 1]):
            result += r_num[roman_string[i + 1]] - c_value
            i += 2
        else:
            result += c_value
            i += 1
    return (result)
