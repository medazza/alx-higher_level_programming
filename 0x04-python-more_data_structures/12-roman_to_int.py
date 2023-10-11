#!/usr/bin/python3

def to_subtract(list_num):
    max_val = max(list_num)
    return (max_val - sum(n for n in list_num if max_val > n))

def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return (0)
    rom_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    last_rom = 0
    list_num = [0]
    for ch in roman_string:
        if ch in rom_n:
            ch_value = rom_n[ch]
            if ch_value <= last_rom:
                num += to_subtract(list_num)
                list_num = [ch_value]
            else:
                list_num.append(ch_value)
            last_rom = ch_value
    num += to_subtract(list_num)
    return (num)
