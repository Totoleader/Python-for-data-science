#!/usr/bin/python3

def all_thing_is_obj(object: any) -> int:
    type_names = {
        list: f"List : {object.__class__}",
        tuple: f"Tuple : {object.__class__}",
        set: f"Set : {object.__class__}",
        dict: f"Dict : {object.__class__}",
        str: f"{object} is in the kitchen : {object.__class__}"
    }
    typename = type_names.get(object.__class__, "not found")

    if typename == "not found":
        print("Type not found")
    else:
        print(typename)
    
    ## VERSION THAT WORKS WITH EVERY TYPE
    # type_name = str(object.__class__).replace("class ", "").strip("<>'").capitalize()
    # if type_name == "Str":
    #     message = f"{object} is in the kitchen : {object.__class__}"
    # else:
    #     message = f"{type_name} : {object.__class__}"
    # print(message)
    return 42