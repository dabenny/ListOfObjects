

def test_list_creation():
    assert "loud noises".upper() == "LOUD NOISES"

def test_reversed():
    assert list(reversed([1, 2, 3, 4])) == [4, 3, 2, 1]

def test_some_primes():
    assert 37 in {
        num
        for num in range(1, 50)
        if num != 1 and not any([num % div == 0 for div in range(2, num)])
    }

from listofobj import ListOfObj

def test_list_creation():
    assert ListOfObj([2,3,4,5,6])

def test_list_type():
    test_list = ListOfObj([2,3,4,5,6])
    assert type(test_list) == ListOfObj

def test_list_iterable():
    test_list = ListOfObj([2,3,4,5,6])
    assert 3 in [x for x in test_list]

def test_list_len():
    test_list = ListOfObj([2,3,4,5,6])
    assert len(test_list) == 5

def test_list_index():
    test_list = ListOfObj([2,3,4,5,6])
    assert test_list[1] == 3

def test_list_slice():
    test_list = ListOfObj([2,3,4,5,6])
    assert test_list[1:2] == [3]

def test_list_slice_type():
    test_list = ListOfObj([2,3,4,5,6])
    assert type(test_list[2:4]) == ListOfObj

def test_list_reverse():
    test_list = ListOfObj([2,3,4,5,6])
    assert test_list[::-1] == [6,5,4,3,2]

def test_list_gt():
    test_list = ListOfObj([2,3,4,5,6])
    assert test_list > 2

def test_list_slice_by_bool():
    test_list = ListOfObj([2,3,4,5,6])
    assert type(test_list[test_list > 2]) == ListOfObj
