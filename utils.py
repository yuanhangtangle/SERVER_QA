#!/usr/bin/python3
import json
with open("./__test__.json", 'r') as f:
    test_config = json.load(f)

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

def at_least_one_in(keywords: list, string: str) -> bool:
    '''
    Check if `string` contains at least one keyword in `keywords`
    :param keywords: list, keywords to match
    :param string: str, the string to match
    :return:
    '''
    for kw in keywords:
        if kw in string:
            return True
    return False

def fill_obj(obj_dest: object, obj_source: object):
    '''
    Fill the attributes whose value is `None` in `obj_dest` with the corresponding attribute in `obj_source`
    :param obj_dest: the obj to fill
    :param obj_source: the source object
    :return:
    '''
    assert type(obj_dest) == type(obj_source), "Two objects must be of the same class"
    for key in obj_dest.__dict__.keys():
        if obj_dest.__dict__[key] is None:
            obj_dest.__dict__[key] = obj_source.__dict__[key]

    return obj_dest

def print_slots(obj: object):
    for key in obj.__dict__.keys():
        print(
            "{}.{} = {}".format(
                obj.__name__, key, obj.__dict__[key]
            )
        )

def set_test_info(basename: str):
    return test_config[basename]