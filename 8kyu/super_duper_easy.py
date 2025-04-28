# https://www.codewars.com/kata/55a5bfaa756cfede78000026/train/python

# Make a function that returns the value multiplied by 50 and increased by 6.
# If the value entered is a string it should return "Error".


# def problem(a):
#     if isinstance(a, int):
#         n = int(a)
#     elif isinstance(a, float):
#         n = float(a)
#     else:
#         return "Error"
#     return int(n * 50 + 6)


# Best practice
def problem(a):
    return "Error" if isinstance(a, str) else int(a * 50 + 6)


print(problem("hello"))
print(problem(1))
print(problem(1.2))
