def existsKeyInDict(key, dict_):
    return key in dict_.keys()


def deleteValueFromListInDict(key, value, dict_):
    try:
        if key == "":
            raise Exception
        
        if value in dict_[key]:
            dict_[key].remove(value)
            return True
        return False
    except KeyError:
        return False
    except ValueError: 
        return False


def swapTaskFromListInDict(key, swapoutvalue, swapinvalue, dict_):
    if existsKeyInDict(key, dict_) and swapoutvalue in dict_[key]:
        dict_[key] = [swapinvalue if value == swapoutvalue else value for value in dict_[key]]
        return True
    return False
