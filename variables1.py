# example 1

age = 22
age1 = input("what is your age?")

result = age + age1

print(result)

# o/p -: This gives an error because In the provided code, age is an integer, and age1 is obtained from user input
# using the input() function. The input() function always returns a string, even if the user enters a numeric value.
# Now, if the user enters a number, let's say "25", the attempt to add an integer (age) to a string (age1) will result
# in a TypeError. In Python, you cannot directly concatenate a string and an integer using the + operator without explicit
# type conversion.


# example 2

age = 22
age1 = input("what is your age?")

result = age + int(age1)

print(result)

# o/p -: 44


# example 3

age2 = input("Enter the age2") # suppose i gave an input 22

result = age1 + age2

print(result)  # o/p -: 2222












