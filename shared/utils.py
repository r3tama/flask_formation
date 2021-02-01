def existsKeyInDict(key, dict_):
    return key in dict_.keys()


def deleteValueFromListInDict(key, value, dict_):
    if value in dict_.get(key,[]):
        dict_[key].remove(value)
        return True
    return False
