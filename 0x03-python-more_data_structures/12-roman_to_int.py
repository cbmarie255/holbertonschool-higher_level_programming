#!/usr/bin/python3
def roman_to_int(roman_string):
    romanNumerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    conversion = 0
    for i, letter in enumerate(roman_string):
        if (i + 1) == len(roman_string) or romanNumerals[letter] >= romanNumerals[roman_string[i + 1]]:
            conversion += romanNumerals[letter]
        else:
            conversion -= romanNumerals[letter]
    return conversion
