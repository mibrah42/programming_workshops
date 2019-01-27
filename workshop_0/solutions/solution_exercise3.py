# Congrats! you've made it to the last exercise 

# Exercise 3
# Complete the functions below
# use the command: py -m pytest -l 
# to test your code in the terminal

# 1. write a function called getAverage that takes a parameter grades which
# is an array of test scores from a scale of 0.0 - 100.0
# the function should return the average of these numbers
def getAverage(grades):
    total = 0
    for grade in grades:
        total += grade 
    return total / len(grades)


# 2. write a function called fizzBuzz that takes the parameter number and returns an array
# loops from the range 1 (inclusive) to number (exclusive)
# if the number is divisible by 3, append 'Fizz' to the array
# if the number is divisible by 5, append 'Buzz' to the array
# if the number is divisible by 3 and 5, append 'FizzBuzz' to the array
# else just append the number as itself 
def fizzBuzz(number):
    result = []
    for i in range(1, number):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(i)
    return result 


# 3. create a function called hasDuplicates which 
# takes in the parameter numbers and returns true if 
# the array of numbers has a duplicate value and false otherwise
def hasDuplicates(numbers):
    return (len(numbers) != len(set(numbers)))

# 4. (optional) write a function called reverseText
# that takes in the parameter text and returns
# the reversed version of it
# hint: search for the following on google
# reversed, string to list conversion, and join
def reverseText(text):
    text = list(text)
    for i in range(len(text)//2):
        temp = text[i]
        text[i] = text[len(text) - i - 1]
        text[len(text) - i - 1] = temp
    return "".join(text)

# def reverseTextShort(text):
#     return "".join(list(reversed(list(text))))

# def reverseTextRecursive(text):
#     if len(text) == 0:
#         return ""
#     return text[len(text) - 1] + reverseTextRecursive(text[:len(text) - 1])
