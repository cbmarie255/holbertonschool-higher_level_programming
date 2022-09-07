#!/usr/bin/python3
def roman_to_int(roman_string):
    romanNs = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    conversion = 0
    if type(roman_string) != str or not roman_string:
        return 0
    for i, letter in enumerate(roman_string):
        if (i+1) == len(roman_string):
            conversion += romanNs[letter]
        elif romanNs[letter] >= romanNs[roman_string[i+1]]:
            conversion += romanNs[letter]
        else:
            conversion -= romanNs[letter]
    return conversion
