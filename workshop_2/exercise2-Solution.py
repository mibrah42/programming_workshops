# Problem Solving Questions
# Source: Cracking the coding interview Chapter 1 (Arrays and Strings)

# 1 is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
def isUniqueWithSet(text):
    if len(text) == len(set(list(text))):
        return True 
    else: 
        return False

def isUniqueNoSet(text):
    for i, letter in enumerate(text):
        for j, other in enumerate(text):
            if i != j and letter == other:
                return False 
    return True

def isUniqueNoSetOptimized(text):
    text = list(text)
    text.sort()
    for i in range(len(text) - 1):
        if text[i] == text[i+1]:
            return False 
    return True

name = "mohamed" # with duplicates
print(isUniqueNoSet(name)) # false
print(isUniqueWithSet(name)) # false
print(isUniqueNoSetOptimized(name)) # false

name = "alex" # no duplicates
print(isUniqueNoSet(name)) # true
print(isUniqueWithSet(name)) # true
print(isUniqueNoSetOptimized(name)) # true

# 2 Check permutation: Given two strings, write a method to decide if one is a permutation of the other.
def checkPermutationBySorting(first, second):
    if len(first) != len(second):
        return False
    first = sorted(first)
    second = sorted(second)
    return first == second

def checkPermutationByCharCount(first, second):
    if len(first) != len(second):
        return False
    counts = {}
    for letter in first:
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1

    for letter in second:
        if letter in counts:
            counts[letter] -= 1
        else:
            return False
    
    for letter in counts:
        if counts[letter] != 0:
            return False 

    return True

print(checkPermutationBySorting("lake", "bake")) # false
print(checkPermutationByCharCount("lake", "bake")) # false
print(checkPermutationBySorting("mohamed", "ohamedm")) # true
print(checkPermutationByCharCount("mohamed", "ohamedm")) # true

# 3 URLify: Write a method to replace all spaces in a string with '%20'. 
# EXAMPLE
# Input: "Mr John Smith ", 13
# Output: "Mr%20John%20Smith"
def URLify(url):
    url = url.strip()
    url = url.replace(" ", "%20")
    return url

print(URLify("Mr John Smith  "))


# 4 Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
# EXAMPLE
# Input: Tact Coa
# Output: True (permutations: "taco cat", "atco eta", etc.)
def isPalindromePermutation(text):
    oddCounter = 0
    charsArray = [0]*26
    text = text.replace(" ", "")
    for letter in text:
        charsArray[ord(letter) - 97] += 1
        if charsArray[ord(letter) - 97] % 2 == 0:
             oddCounter -= 1
        else:
            oddCounter += 1
    if oddCounter > 1:
        return False 
    return True
    
print(isPalindromePermutation("taco cat")) # true
print(isPalindromePermutation("taco ca")) # false
# Another solution is to create a dictionary with character counts and then iterate through it and determine if there is an odd value


# 5. String Compression: Implement a method to perform basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the "compressed" string would not become smaller than the original string, your method should return the original string. You can assume the string has only uppercase and lowercase letters(a - z).
def stringCompression(text):
    compressed = text[0]
    counter = 1
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            counter += 1
        else:
            compressed += str(counter)
            compressed += text[i]
            counter = 1

        if i == (len(text) - 1):
            compressed += str(counter)

    if len(compressed) >= len(text):
        return text

    return compressed


print(stringCompression("aabcccccaaa"))
print(stringCompression("abcca"))
