#!/usr/bin/python3

def is_even(num: int):
    '''check if input int is even'''
    return num % 2 == 0

def is_digit(character: str):
    '''check if input str is all digit'''
    return character.isdigit()
    
def ft_filter(function, iterable):
    '''Return an iterator yielding those items of iterable for which function(item) is true. If function is None, return the items that are true.'''
    result = [x for x in iterable if function(x)]
    return iter(result)


def main():
    '''Tests implementation of ft_filter'''
    initlist = [1, 2, 3, 4]
    initlist2 = ["1", "2", "3r", "4"]

    initlist_ = ft_filter(is_even, initlist)
    filteredlist = list(initlist_)

    initlist_2 = ft_filter(is_digit, initlist2)
    filteredlist2 = list(initlist_2)

    print(filteredlist)
    print(filteredlist2)

if __name__ == "__main__":
    main()