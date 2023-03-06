# Working with lists
# When you want to do the same action with every item in a list, you
# can use Python’s for loop.
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

print()

for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
print("Thank you, everyone. That was a great magic show!\n")

# Making Numerical Lists
# Lists are ideal for storing sets of numbers, and Python provides a variety
# of tools to help you work efficiently with lists of numbers. Once you
# understand how to use these tools effectively, your code will work well
# even when your lists contain millions of items.

# Using the range() Function
# Python’s range() function makes it easy to generate a series of numbers.

for value in range(1, 5):
    print(value)

# Using range() to Make a List of Numbers
numbers = list(range(1, 6))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

odd_numbers = list(range(1, 10, 2))
print(odd_numbers)

squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print(squares)

# Simple Statistics with a List of Numbers
# A few Python functions are helpful when working with lists of numbers. For
# example, you can easily find the minimum, maximum, and sum of a list of
# numbers:
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

# List Comprehensions
# The approach described earlier for generating the list squares consisted of
# using three or four lines of code. A list comprehension allows you to
# generate this same list in just one line of code.
squares = [value ** 2 for value in range(1, 11)]
print(squares)

# Working with Part of a List
# Slicing a List
# To make a slice, you specify the index of the first and last elements you
# want to work with. As with the range() function, Python stops one item
# before the second index you specify.
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

# If you omit the first index in a slice, Python automatically starts your
# slice at the beginning of the list:
print(players[:3])

# A similar syntax works if you want a slice that includes the end of a list.
# For example, if you want all items from the third item through the last item,
# you can start with index 2 and omit the second index:
print(players[2:])

# if we want to output the last three players on the roster, we can use
# the slice players[-3:]:
print(players[-3:])

# Looping Through a Slice
# You can use a slice in a for loop if you want to loop through a subset of the
# elements in a list.
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

# Copying a List
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods.copy()
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

# shalow copy with slice
uma_lista = my_foods[:]
print(uma_lista.pop(), uma_lista, my_foods, sep='\n')

# Tuples
# sometimes you’ll want to create a list of items that cannot change.
# Tuples allow you to do just that. Python refers to values that cannot change
# as immutable, and an immutable list is called a tuple.
# A tuple looks just like a list, except you use parentheses instead of square
# brackets.
# Tuples are technically defined by the presence of a comma; the parentheses
# make them look neater and more readable. If you want to define a tuple with
# one element, you need to include a trailing comma.
uma_tupla = (3,)
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)
