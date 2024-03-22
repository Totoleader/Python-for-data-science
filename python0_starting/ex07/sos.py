#!/usr/bin/python3

import sys

def string_to_morse(string: str):
    morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-',
        'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-',
        'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----',
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/',
    }
    output_string = ""

    for letter in string:
        if letter.isalnum() or letter == " ":
            output_string += f"{morse_code_dict[letter]} "
        else:
            raise AssertionError("the arguments are bad")
    print(output_string)

def main():
    try:
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")
        else:
            string_to_morse(sys.argv[1])
    except AssertionError as e:
        print("AssertionError: {e}")

if __name__ == "__main__":
    main()