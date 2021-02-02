def existsKeyInDict(key, dict_):
    return key in dict_.keys()


def deleteValueFromListInDict(key, value, dict_):
    try:
        if key == "":
            raise Exception
        
        value in dict_[key]
        dict_[key].remove(value)
        
        return True
    except KeyError:
        return False
    except ValueError: 
        return False
    
