#!/usr/bin/python3

def clear(obj: object) -> bool:
    '''
    Set all the attribute in obj as `None`
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
