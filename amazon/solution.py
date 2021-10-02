"""
Problem: Given an encrypted string s, and an integer k,
shift all of the letters in s by k characters counter clockwise.

For example:
s = "abcde", k = 1 would return "zabcd". 

If k is negative, this would shift the string to the right by k characters.
For Example:
s = "abcde", k = -5 would return "fghij".
"""
import string


def translate_char(char, k):
    # grab all uppercase ascii
    letters = string.ascii_uppercase[:26]
    letters_to_index = {}
    negative = False
    return_char = char
    # map letter to index
    for i in range(0, 26):
        letters_to_index[letters[i]] = i
    if k < 0:
        negative = True
    if k >= 26:
        k = k % 26
    # grab char index
    index = letters_to_index[char]
    for i in range(1, abs(k) + 1):
        if negative:
            index += 1
            if index == 26:
                index = 0
        else:
            index -= 1
        return_char = letters[index]
    return return_char


def translate_string(string, k):
    translated = ""
    for letter in string.upper():
        translated += translate_char(letter, k)

    return translated


print(translate_string('A', 27))
