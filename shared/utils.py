def existsKeyInDict(key, dict_):
    return key in dict_.keys()

def deleteValueFromDict(key, value, dict_):
    if value in dict_[key]:
        dict_[key].remove(value)
        return True
    return False