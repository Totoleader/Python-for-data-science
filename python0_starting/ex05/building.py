#!/usr/bin/python3

import sys

def count_chars(input_string: str):
    '''counts and prints alphanum, space and ponctuations characters in string'''
    ponctuations = {".", ",", ":", ";", "!", "?"}
    upperCount = 0
    lowerCount = 0
    ponctuationCount = 0
    spaceCount = 0
    digitCount = 0

    for char in input_string:
        if char.islower():
            lowerCount += 1
        elif char.isspace():
            spaceCount += 1
        elif char.isupper():
            upperCount += 1
        elif char in ponctuations:
            ponctuationCount += 1
        elif char.isdigit():
            digitCount += 1

    total = upperCount + lowerCount + ponctuationCount + spaceCount + digitCount
    print("The text countains", total, "characters:")
    print(upperCount, "upper letters")
    print(lowerCount, "lower letters")
    print(ponctuationCount, "ponctuations marks")
    print(spaceCount, "spaces")
    print(digitCount, "digits")


def main():
    '''Counts characters in string passed as argument'''
    try:
        if len(sys.argv) != 2:
            raise AssertionError("Must have a single string as argument.")
        else:
            count_chars(sys.argv[1])

    except AssertionError as e:
        print(f"AssertionError: {e}")
        string = input("Enter string: ")
        count_chars(string)
    


if __name__ == "__main__":
    main()
