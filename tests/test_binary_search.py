from array_binary_search.binary_search import get_length
from array_binary_search.binary_search import binary_search


def test_get_length0():
    source_list1 = []
    expected = 0
    actual = get_length(source_list1)
    assert expected == actual

def test_get_length1():
    source_list1 = [2,4,6,8]
    expected = 4
    actual = get_length(source_list1)
    assert expected == actual

def test_get_length2():
    source_list2 = [4,8,15,23,42]
    expected = 5
    actual = get_length(source_list2)
    assert expected == actual

def test_binary_serach0():
    input_list = [4,8,15,16,23,42]
    key = 4
    expected = 0
    actual = binary_search(input_list, key)
    assert expected == actual

def test_binary_search1():
    input_list = [4,8,15,16,23,42]
    key = 8
    expected = 1
    actual = binary_search(input_list, key)
    assert expected == actual

def test_binary_search2():
    input_list = [4,8,15,16,23,42]
    key = 15
    expected = 2
    actual = binary_search(input_list, key)
    assert expected == actual

def test_binary_search3():
    input_list = [4,8,15,16,23,42]
    key = 16
    expected = 3
    actual = binary_search(input_list, key)
    assert expected == actual

def test_binary_search4():
    input_list = [4,8,15,16,23,42]
    key = 23
    expected = 4
    actual = binary_search(input_list, key)
    assert expected == actual

def test_binary_search5():
    input_list = [4,8,15,16,23,42]
    key = 42
    expected = 5
    actual = binary_search(input_list, key)
    assert expected == actual

def test_binary_search6():
    input_list = [11,22,33,44,55,66,77]
    key = 90
    expected = -1
    actual = binary_search(input_list, key)
    assert expected == actual