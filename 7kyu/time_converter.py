# https://www.codewars.com/kata/56b8b0ae1d36bb86b2000eaa/train/python

# Given a time in a time format class, return it without year, month and day.

# It should return a string including milliseconds with 3 decimals.

# Example:

# datetime(2016, 2, 8, 16, 42, 59)
# #Should return:
# "16:42:59,000"
from datetime import datetime


# def convert(time):
#     return (
#         f"{time.hour:02}:{time.minute:02}:{time.second:02},{time.microsecond//1000:03}"
#     )


# Best practice
def convert(time):
    return time.time().strftime("%X,%f")[:-3]


print(convert(datetime(2016, 2, 8, 16, 42, 59)))
print(convert(datetime(1951, 10, 31, 2, 2, 24, 399000)))
print(convert(datetime(1523, 5, 29, 23, 2, 2, 9000)))
print(convert(datetime(1, 1, 1, 1, 1, 1, 110000)))
print(convert(datetime(9999, 9, 9, 9, 9, 9, 999999)))
print(convert(datetime(2, 12, 30, 23, 59, 59, 875939)))
print(convert(datetime(1850, 12, 30, 13, 39, 19)))
print(convert(datetime(1978, 3, 18, 12, 0, 0, 0)))
print(convert(datetime(1850, 12, 30, 11, 11, 11, 123939)))
print(convert(datetime(1850, 12, 30, 0, 0, 0, 321939)))
