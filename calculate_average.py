# https://www.codewars.com/kata/57a2013acf1fa5bfc4000921/train/python
# Write a function which calculates the average of the numbers in a given array.

# Note: Empty arrays should return 0.


def find_average(numbers):
    if len(numbers) == 0:
        return 0
    sum = 0
    for n in numbers:
        sum += n
    return sum / len(numbers)


# Best practice
def find_average(array):
    return sum(array) / len(array) if array else 0


print(find_average([1, 2, 3]))
print(find_average([]))
print(find_average([1, 2]))
