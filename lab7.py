
import pytest
from typing import List


# Accepts a list of integers
def initializeMinMaxList(myList: List[int]) -> None:  # given
    myList.sort()


def insertItem(myList: List[int], item: int) -> None:  # given
    myList.append(item)
    myList.sort()


def getMinMax(myList: List[int], minormax: str) -> int:  # given -- but requires additional assert
    assert minormax.upper() == "MAX" or minormax.upper() == "MIN", "2nd argument must be 'Min' or 'Max' "
    listlength = len(myList)
    assert listlength != 0, "List cannot be empty."
    result: int
    if minormax.upper() == "MAX":
        result = myList[-1]
        del myList[-1]
    else:
        result = myList[0]
        del myList[0]
    return result


def test_getMinMaxCase1():
    a = [99, 20]
    initializeMinMaxList(a)
    result_max = getMinMax(a, "MAX")
    assert result_max == 99, "Error – should be 99"
    result_min = getMinMax(a, "MIN")
    assert result_min == 20, "Error – should be 20"


def test_getMinMaxCase2():
    y = [1]
    initializeMinMaxList(y)
    result_max = getMinMax(y, "MAX")
    assert result_max == 1, "Error – should be 1"
    insertItem(y, 1)
    result_min = getMinMax(y, "MIN")
    assert result_min == 1, "Error – should be 1"


def test_getMinMaxCase3():
    empty = []
    x = 2
    y = 5
    initializeMinMaxList(empty)
    insertItem(empty, x), insertItem(empty, y)
    result_max = getMinMax(empty, "MAX")
    assert result_max == 5, "Error – should be 5"
    result_min = getMinMax(empty, "MIN")
    assert result_min == 2, "Error – should be 2"


def test_getMinMaxRequestError():
    list = [5, 2, 3]
    initializeMinMaxList(list)
    with pytest.raises(AssertionError) as error:
        result = getMinMax(list, "MID")
    assert error.typename == "AssertionError", "Should raise AssertionError!"


def test_getMinMaxEmptyError():
    empty = []
    initializeMinMaxList(empty)
    with pytest.raises(AssertionError) as error:
        result = getMinMax(empty, "MAX")
    assert error.typename == "AssertionError", "Should raise AssertionError!"


# Main function is given.
def main():
    aList = [10, 11, 99, 1, 55, 100, 34, 88]
    print("Starting List: ", aList)
    initializeMinMaxList(aList)
    min1 = getMinMax(aList, "MIN")
    print("1st min: %d" % (min1))
    min2 = getMinMax(aList, "MIN")
    print("2nd min: %d" % (min2))
    max1 = getMinMax(aList, "MAX")
    print("1st max: %d" % (max1))
    max2 = getMinMax(aList, "MAX")
    print("2nd max: %d" % (max2))

    print("Insert %d %d %d %d" % (min1 - 1, min2 - 1, max1 + 1, max2 + 1))
    insertItem(aList, min1 - 1)
    insertItem(aList, min2 - 1)
    insertItem(aList, max1 + 1)
    insertItem(aList, max2 + 1)

    min1 = getMinMax(aList, "MIN")
    print("1st min: %d" % (min1))
    min2 = getMinMax(aList, "MIN")
    print("2nd min: %d" % (min2))
    max1 = getMinMax(aList, "MAX")
    print("1st max: %d" % (max1))
    max2 = getMinMax(aList, "MAX")
    print("2nd max: %d" % (max2))

    print("DONE.  Type Enter to exit.")
    input()


if __name__ == "__main__":
    main()
