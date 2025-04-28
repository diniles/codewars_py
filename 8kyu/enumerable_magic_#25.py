# https://www.codewars.com/kata/545afd0761aa4c3055001386/train/python

# Create a function that accepts a list/array and a number n, and returns a
# list/array of the first n elements from the list/array.

# If you need help, here's a reference:

# https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range


def take(arr, n):
    return arr[:n]


print(take([0, 1, 2, 3, 5, 8, 13], 3))
