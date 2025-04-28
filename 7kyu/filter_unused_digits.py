# https://www.codewars.com/kata/55de6173a8fbe814ee000061

# Description:
# Given a varying number of integer arguments, return the digits that are not
# present in any of them.

# Example:

# [12, 34, 56, 78]  =>  "09"
# [2015, 8, 26]     =>  "3479"


# def unused_digits(*numbers):
#     result = ""
#     string = "".join(str(val) for val in numbers)
#     for i in range(10):
#         if str(i) not in string:
#             result += str(i)
#     return result


# Best practice
def unused_digits(*args):
    return "".join(number for number in "0123456789" if number not in str(args))


print(unused_digits(12, 34, 56, 78))
print(unused_digits(2015, 8, 26))
print(unused_digits(276, 575))
print(unused_digits(643))
print(unused_digits(864, 896, 744))
