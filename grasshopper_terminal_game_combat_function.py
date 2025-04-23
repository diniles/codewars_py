# https://www.codewars.com/kata/586c1cf4b98de0399300001d/train/python

# Create a combat function that takes the player's current health and the
# amount of damage received, and returns the player's new health. Health
# can't be less than 0.


# def combat(health, damage):
#     rest = health - damage
#     return 0 if rest < 0 else rest


# Beast practice
def combat(health, damage):
    return max(0, health - damage)


print(combat(100, 5))
print(combat(83, 16))
print(combat(20, 30))
