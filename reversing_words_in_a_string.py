# https://www.codewars.com/kata/57a55c8b72292d057b000594/train/python
# You need to write a function that reverses the words in a given string.
# Words are always separated by a single space.

# As the input may have trailing spaces, you will also need to ignore
# unneccesary whitespace.

# Example (Input --> Output)


# "Hello World" --> "World Hello"
# "Hi There." --> "There. Hi"
# def reverse(st):
#     lst = st.split()
#     lst.reverse()
#     return " ".join(lst)


# Best practice
def reverse(st):
    # Your Code Here
    return " ".join(st.split()[::-1])


print(reverse("Hello World"))
print(reverse("Hi There."))
