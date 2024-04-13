#!/usr/bin/python3
import math

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    '''Input a list of height and a list of weight and returns a list of BMI (Body Mass Index)'''
    # return [single_height / pow(single_weight, 2) for single_height, single_weight in zip(height, weight)]
    try:
        if len(weight) != len(height):
            raise ValueError("Weight list and height list are not the same size.")
        bmi_list = []
        for heights, weights in zip(height, weight):
            bmi_list.append(heights / (weights ** 2))
        return bmi_list
    except ValueError as error:
        print(f"Error: {error}")
        return []
        

    
def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    '''Checks if BMIs in the input list are above input BMI limit'''
    return [value > limit for value in bmi]
#your code here

def main():
    weights = [2, 3, 4]
    heights = [1, 2, 3]
    bmi = give_bmi(heights, weights)

    for values in bmi:
        print(values)
    
    bust_limit = apply_limit(give_bmi(heights, weights), 0.2)
    for values in bust_limit:
        print(values)

    # print("yo")

if __name__ == "__main__":
    main()