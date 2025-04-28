# https://www.codewars.com/kata/582c81d982a0a65424000201/train/python

# Is every value in the array an array?

# This should only test the second array dimension of the array. The values
# of the nested arrays don't have to be arrays.

# Examples:

# [[1],[2]] => true
# ['1','2'] => false
# [{1:1},{2:2}] => false


def arr_check(arr):
    return all(type(el) is list for el in arr)


print(arr_check([]))
print(arr_check([["string"]]))
print(arr_check([[], {}]))
print(arr_check([[1], [2], [3]]))
print(arr_check(["A", "R", "R", "A", "Y"]))
