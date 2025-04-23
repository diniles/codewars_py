# https://www.codewars.com/kata/5761a717780f8950ce001473/train/python

# Philip's just turned four and he wants to know how old he will be in
# various years in the future such as 2090 or 3044. His parents can't keep
# up calculating this so they've begged you to help them out by writing a
# programme that can answer Philip's endless questions.

# Your task is to write a function that takes two parameters: the year of
# birth and the year to count years in relation to. As Philip is getting more
# curious every day he may soon want to know how many years it was until he
# would be born, so your function needs to work with both dates in the future
# and in the past.

# Provide output in this format: For dates in the future: "You are ... year(s) old."
# For dates in the past: "You will be born in ... year(s)." If the year of birth
# equals the year requested return: "You were born this very year!"

# "..." are to be replaced by the number, followed and proceeded by a single space.
# Mind that you need to account for both "year" and "years", depending on the result.


def calculate_age(year_of_birth, current_year):
    diff = current_year - year_of_birth
    year = "year" if abs(diff) == 1 else "years"
    if diff > 0:
        return f"You are {diff} {year} old."
    elif diff < 0:
        return f"You will be born in {abs(diff)} {year}."
    else:
        return "You were born this very year!"


print(calculate_age(2012, 2016))
print(calculate_age(1989, 2016))
print(calculate_age(2000, 2090))
print(calculate_age(2000, 1990))
print(calculate_age(2000, 2000))
print(calculate_age(900, 2900))
print(calculate_age(2010, 1990))
print(calculate_age(2010, 1500))
print(calculate_age(2011, 2012))
print(calculate_age(2000, 1999))
