#!/usr/bin/python3

import math

def NULL_not_found(object: any) -> int:
    type_names = {
        None: f"Nothing : {object} {object.__class__}",
        math.nan: f"Cheese : {object} {object.__class__}",
        0: f"Zero : {object} {object.__class__}",
        "": f"Empty : {object} {object.__class__}",
        False: f"Fake : {object} {object.__class__}"
    }
    typename = type_names.get(object, "not NULL or not found")

    if object.__class__ is bool and object == False:
        typename = f"Fake : {object} {object.__class__}"
    
    if typename == "not NULL or not found":
        print("Type not found")
        return 1
    else:
        print(typename)
        return 0