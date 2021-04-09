#!/usr/bin/python3

def clear(obj: object) -> bool:
    '''
    Set all the attributes in `obj` as `None`
    :param obj: any object
    :return: True if success, else False
    '''
    try:
        for key in obj.__dict__.keys():
            obj.__dict__[key] = None
        return True
    except:
        print("ERROR OCCUR WHEN CLEARING THE GIVEN OBJ")
        return False

def is_filled(obj: object) -> bool:
    '''
    Check if a slot class is fully filled (all the slots are filled)
    :param obj: a slot object defined in `slotValues.py`, e.g. Server, User, etc.
    :return: True if `obj` is filled, else False
    '''
    filled = True
    for key in obj.__dict__.keys():
        if obj.__dict__[key] is None:
            filled = False
            break
    return filled
