#!/usr/bn/python3
def roman_to_int(roman_string):
    if roman_string == None or type(roman_string) != str:
        return (0)
    dic = {
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
        c_value = dic.get(c_char)
        if not c_value:
            return (0)
        if i + 1 < len(roman_string) and c_value < dic.get(roman_string[i + 1]):
            result += dic[roman_string[i + 1]] - c_value
            i += 2
        else:
            result += c_value
            i += 1
    return (result)
