#!/usr/bin/python3
def to_subtract(list_num):
    subtract = 0
    maxlist = max(list_num)

    for i in list_num:
        if max_list > i:
            subtract += i

    return (maxlist - subtract)
def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    rom_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    keyslist = list(rom_num.keys())

    number = 0
    roman_last = 0
    list_num = [0]

    for x in roman_string:
        for rom_number in keyslist:
            if rom_number == x:
                if rom_num.get(x) <= roman_last:
                    number += to_subtract(list_num)
                    list_num = [rom_num.get(x)]
                else:
                    list_num.append(rom_num.get(x))

                roman_last = rom_num.get(x)

    number += to_subtract(list_num)

    return (number)

