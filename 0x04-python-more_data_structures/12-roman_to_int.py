#!/usr/bn/python3

def roman_to_int(roman_string):
    roman_dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    if type(roman_string) != str or roman_string == None:
        return (0)
    for i, char in enumerate(roman_string):
        temp = roman_dic[char]
        try:
            if temp < roman_dic[roman_string[i + 1]]:
                temp = temp * -1
            except IndexError:
                pass
            num = num + temp
        return (num)
