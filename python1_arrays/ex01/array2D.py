#!/usr/bin/python3
import numpy as np

def slice_me(family: list, start: int, end: int) -> list:
    '''Takes in a matrix (family) and crops it to '''

    if (family.ndim != 2):
        print("Invalid : Array is not 2 dimentionnal")
        return family    

    print(f"My shape is : {family.shape}")
    cropped_array = family[start:end]
    print(f"My new shape is : {cropped_array.shape}")
    # print(slice_me(cropped_array))

    return cropped_array


def main():
    array2slice = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
    print(slice_me(array2slice, 1, -1))


if __name__ == "__main__":
    main()