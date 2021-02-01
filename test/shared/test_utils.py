from shared.utils import deleteValueFromListInDict, existsKeyInDict
import pytest

TEST_DIC = {
    "list1": ["task1","task2","task3"],
    "list2": ["task1"],
    "list3": []
}

EMPTY_TEST_DIC = {}

@pytest.mark.parametrize("data", ["list1","list2","list3"])
def test_existsKeyInDict_givenExistingKey(data): 
    assert existsKeyInDict(data,TEST_DIC) 

@pytest.mark.parametrize("data", ["list4","list5","list6"])
def test_existsKeyInDict_withoutExistingKey(data):
    assert not existsKeyInDict(data,TEST_DIC) 

def test_existsKeyInDict_givenEmptyDict():
    assert not existsKeyInDict("list5",EMPTY_TEST_DIC)

@pytest.mark.parametrize("data", ["task1","task2","task3"])
def test_deleteValueFromListInDict_givenExistingKeyAndValue(data):
    assert deleteValueFromListInDict("list1",data,TEST_DIC)  

@pytest.mark.parametrize("data", ["task4","task5","task6"])
def test_deleteValueFromListInDict_givenExistingKeyAndWithoutExistingValue(data):
    assert not deleteValueFromListInDict("list1",data,TEST_DIC)

def test_deleteValueFromListInDict_withoutExistingKey():
    assert not deleteValueFromListInDict("list6","task1",TEST_DIC)

def test_deleteValueFromListInDict_givenEmptyDic():
    assert not deleteValueFromListInDict("list1","task1",EMPTY_TEST_DIC)