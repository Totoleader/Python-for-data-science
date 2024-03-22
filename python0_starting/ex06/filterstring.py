#!/usr/bin/python3
import sys
from ft_filter import ft_filter

def listBiggerThanN(string: str, n: int):
    splitted_words = string.split(" ")
    filtered_list = ft_filter(lambda x: len(x) > n, splitted_words)
    return list(filtered_list)

def main():
    try:
        try:
            if len(sys.argv) != 3 or not sys.argv[1].isprintable() or not sys.argv[1]:
                raise AssertionError("the arguments are bad")
            else:
                string = sys.argv[1]
                nb = int(sys.argv[2])
                print(listBiggerThanN(string, nb))


        except ValueError:
            raise AssertionError("the arguments are bad")
            
            
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()