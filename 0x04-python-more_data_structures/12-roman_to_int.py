#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for i, c in enumerate(roman_string):
        if (i+1) == len(roman_string) or int[c] >= int[roman_string[i+1]]:
            result += int[c]
        else:
            result -= int[c]
    return result
