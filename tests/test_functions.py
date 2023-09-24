import json
from programm import functions

def test_get_operations():
    assert get_operations("operations.json")
def test_get_executed_operations():
    assert get_executed_operations([{"key":"value"},{"item":"items"}]) == []

def test_sort_by_date():
    assert sort_by_date([3,5,4,2,1]) == [5,4,3,2,1]

def test_finish_operation():
    pass
