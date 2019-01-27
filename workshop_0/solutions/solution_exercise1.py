from math import pi

# Exercise 1
# Complete the functions below
# use the command: py -m pytest -l 
# to test your code in the terminal


# 1. write a function add that takes the parameters x and y
# and returns the sum
def add(x,y):
    return x + y

# 2. write a function called square that takes the parameter x
# and returns the square of it
def square(x):
    return x ** 2

# 3. write a function called area that takes a radius r as a parameter
# and returns the area of a circle with radius r
# hint: use the pi constant from the math library
# formula: pi*r^2
def area(r):
    return pi * (r ** 2)

# 4. Create a function called calculateInterestRate that takes in 2 parameters
# interest: amount added to the original investment
# principal: original investment
# and return the interest rate using the following formula
# formula: rate = (interest / principal) * 100
def calculateInterestRate(interest, principal):
    return (interest / principal ) * 100





    