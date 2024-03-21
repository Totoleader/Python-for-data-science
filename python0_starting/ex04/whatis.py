#!/usr/bin/python3
import sys

def whatis(nb: int):
    if nb % 2:
        print("I'm odd.")
    else:
        print("I'm even.")

args = sys.argv

try:

    if len(args) != 2:
        raise AssertionError("must have one argument")
    try:
        value = int(args[1])
    except ValueError:
        raise AssertionError("argument is not an integer")

except AssertionError as e:
    print("AssertionError:", e)
    exit()


whatis(value)
