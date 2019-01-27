# Exercise 2
# Complete the functions below
# use the command: py -m pytest -l 
# to test your code in the terminal

# 1. write a function called getFullName that takes the parameters firstName and lastName
# and returns a string with the full name using string concatenation
# note: make sure to leave space between between the two names
def getFullName(firstName, lastName):
    return f"{firstName} {lastName}"

# 2. write a function called canVote that takes in one parameter: age
# and returns "you can vote !" if the age is greater than or equal to 18
# and returns "you can't vote !" otherwise  
def canVote(age):
    if age >= 18:
        return "you can vote !"
    else:
        return "you can't vote !"


# 3. write a function called isEven that takes in a number
# and returns true if the number is even and false otherwise
# note: make use of the modulus operator %
def isEven(number):
    if number % 2 == 0:
        return True
    else:
        return False


# 4. write a function called cheapChatbot which takes in the parameter message
# if the message is "good morning" return "would you like some coffee?"
# else if the message is "good afternoon" return "good afternoon to you too"
# else if the message is "good evening" return "go to sleep"
# else return "I don't know what you're saying"
# note: make sure the strings match exactly
def cheapChatbot(message):
    if message == "good morning":
        return "would you like some coffee?"
    elif message == "good afternoon":
        return "good afternoon to you too"
    else:
        return "I don't know what you're saying"


# 5. write a function called favoriteCities with the parameter cities
# take 3 user inputs for city1, city2, and city3 
# add all the inputs to the cities array and return it
def favoriteCities(cities):
    city1 = input("enter city 1: ")
    city2 = input("enter city 2: ")
    city3 = input("enter city 3: ")
    cities.extend([city1, city2, city3])
    return cities