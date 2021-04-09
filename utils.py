#!/usr/bin/python3

def clear(obj: object) -> bool:
    try:
        for key in obj.__dict__.keys():
            obj.__dict__[key] = None
        return True
    except:
        print("ERROR OCCUR WHEN CLEARING THE GIVEN OBJ")
        return False
