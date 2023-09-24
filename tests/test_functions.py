from src.functions import sort_by_date

def test_sort_by_date():
    assert sort_by_date([4,5,2,1,3]) == [1,2,3,4,5]