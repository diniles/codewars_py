# https://www.codewars.com/kata/56cd44e1aa4ac7879200010b/train/python

# Create a method to see whether the string is ALL CAPS.

# Examples (input -> output)
# "c" -> False
# "C" -> True
# "hello I AM DONALD" -> False
# "HELLO I AM DONALD" -> True
# "ACSKLDFJSgSKLDFJSKLDFJ" -> False
# "ACSKLDFJSGSKLDFJSKLDFJ" -> True


def is_uppercase(inp):
    return inp == inp.upper()


print(is_uppercase("c"))
print(is_uppercase("C"))
print(is_uppercase("hello I AM DONALD"))
print(is_uppercase("HELLO I AM DONALD"))
print(is_uppercase("ACSKLDFJSgSKLDFJSKLDFJ"))
print(is_uppercase("ACSKLDFJSGSKLDFJSKLDFJ"))
