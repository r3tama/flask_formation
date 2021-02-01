from shared.utils import deleteValueFromListInDict, existsKeyInDict
import pytest

TEST_DIC = {
    "list1": ["task1","task2","task3"],
    "list2": ["task1"],
    "list3": []
}

EMPTY_TEST_DIC = {}

@pytest.mark.parametrize("data, expected", [("list1",True),("list2",True),("list3",True)])
def test_existsKeyInDict_givenExistingKey(data,expected): 
    assert existsKeyInDict(data,TEST_DIC) == expected

@pytest.mark.parametrize("data, expected", [("list4",False),("list5",False),("list6",False)])
def test_existsKeyInDict_withoutExistingKey(data,expected):
    assert existsKeyInDict(data,TEST_DIC) == expected

def test_existsKeyInDict_givenEmptyDict():
    assert not existsKeyInDict("list5",EMPTY_TEST_DIC)

@pytest.mark.parametrize("data, expected", [("task1",True),("task2",True),("task3",True)])
def test_deleteValueFromListInDict_givenExistingKeyAndValue(data,expected):
    assert deleteValueFromListInDict("list1",data,TEST_DIC) == expected  

@pytest.mark.parametrize("data, expected", [("task4",False),("task5",False),("task6",False)])
def test_deleteValueFromListInDict_givenExistingKeyAndWithoutExistingValue(data,expected):
    assert not deleteValueFromListInDict("list1",data,TEST_DIC)

def test_deleteValueFromListInDict_withoutExistingKey():
    assert not deleteValueFromListInDict("list6","task1",TEST_DIC)

def test_deleteValueFromListInDict_givenEmptyDic():
    assert not deleteValueFromListInDict("list1","task1",EMPTY_TEST_DIC)