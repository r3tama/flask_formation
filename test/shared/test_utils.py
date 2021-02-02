from shared.utils import deleteValueFromListInDict, existsKeyInDict, swapTaskFromListInDict
import pytest,copy

DIC = {
    "list1": ["task1","task2","task3"],
    "list2": ["task1"],
    "list3": []
}


EMPTY_TEST_DIC = {}

@pytest.mark.parametrize("data", ["list1","list2","list3"])
def test_existsKeyInDict_givenExistingKey(data): 
    TEST_DIC=copy.deepcopy(DIC)
    assert existsKeyInDict(data,TEST_DIC) 

@pytest.mark.parametrize("data", ["list4","list5","list6"])
def test_existsKeyInDict_withoutExistingKey(data):
    TEST_DIC=copy.deepcopy(DIC)
    assert not existsKeyInDict(data,TEST_DIC) 

def test_existsKeyInDict_givenEmptyDict():
    assert not existsKeyInDict("list5",EMPTY_TEST_DIC)

@pytest.mark.parametrize("data", ["task1","task2","task3"])
def test_deleteValueFromListInDict_givenExistingKeyAndValue(data):
    TEST_DIC=copy.deepcopy(DIC)
    assert deleteValueFromListInDict("list1",data,TEST_DIC)  

@pytest.mark.parametrize("data", ["task4","task5","task6"])
def test_deleteValueFromListInDict_givenExistingKeyAndWithoutExistingValue(data):
    TEST_DIC=copy.deepcopy(DIC)
    assert not deleteValueFromListInDict("list1",data,TEST_DIC)

def test_deleteValueFromListInDict_withoutExistingKey():
    TEST_DIC=copy.deepcopy(DIC)
    assert not deleteValueFromListInDict("list6","task1",TEST_DIC)

def test_deleteValueFromListInDict_givenEmptyDic():
    assert not deleteValueFromListInDict("list1","task1",EMPTY_TEST_DIC)

def test_deleteValueFromListInDict_givenEmptyKey():
    with pytest.raises(Exception):
        deleteValueFromListInDict("","task1",TEST_DIC)

def test_swapTaskFromListInDict_withoutExistingKey(): 
    TEST_DIC=copy.deepcopy(DIC)
    assert not swapTaskFromListInDict("list6","task1","task2",TEST_DIC)

def test_swapTaskFromListInDict_givenEmptyKey(): 
    TEST_DIC=copy.deepcopy(DIC)
    assert not swapTaskFromListInDict("","task1","task2",TEST_DIC)

def test_swapTaskFromListInDict_givenExistingKeyAndWithoutExistingSwapoutValue():
    TEST_DIC=copy.deepcopy(DIC)
    assert not swapTaskFromListInDict("list2","task2","task5",TEST_DIC)

def test_swapTaskFromListInDict_givenEmptyDict():
    assert not swapTaskFromListInDict("list1","task1","task5",EMPTY_TEST_DIC)

def test_swapTaskFromListInDict_givenExistingKeyAndExistingSwapoutValue():
    TEST_DIC=copy.deepcopy(DIC)
    assert swapTaskFromListInDict("list1","task1","task5",TEST_DIC) 
 
