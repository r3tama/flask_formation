from shared.utils import deleteValueFromListInDict, existsKeyInDict
import pytest

TEST_DIC = {
    "list1": ["task1","task2","task3"],
    "list2": ["task1"],
    "list3": []
}

EMPTY_TEST_DIC = {}

def test_existsKeyInDict_givenExistingKey():
    return_value = existsKeyInDict("list1",TEST_DIC)
    assert return_value

def test_existsKeyInDict_withoutExistingKey():
    return_value = existsKeyInDict("list4",TEST_DIC)
    assert not return_value

def test_existsKeyInDict_givenEmptyDict():
    return_value = existsKeyInDict("list5",EMPTY_TEST_DIC)
    assert not return_value

def test_deleteValueFromListInDict_givenExistingKeyAndValue():
    return_value = deleteValueFromListInDict("list1","task1",TEST_DIC)
    assert return_value

def test_deleteValueFromListInDict_givenExistingKeyAndWithoutExistingValue():
    return_value = deleteValueFromListInDict("list1","task6",TEST_DIC)
    assert not return_value

def test_deleteValueFromListInDict_withoutExistingKey():
    return_value = deleteValueFromListInDict("list1","task5",TEST_DIC)
    assert not return_value

def test_deleteValueFromListInDict_givenEmptyDic():
    return_value = deleteValueFromListInDict("list1","task1",EMPTY_TEST_DIC)
    assert not return_value