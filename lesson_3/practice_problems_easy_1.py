"1. Will the code below raise an error?"

# numbers = [1, 2, 3]
# numbers[6] = 5

'''
Yes, the code will raise an error, because it is tryuing to access an index
that is not in range.
'''
# --- 

'''
2. How can you determine whether a given string ends with an exclamation mark 
(!)? Write some code that prints True or False depending on whether the string 
ends with an exclamation mark.'''

# str1 = "Come over here!"  # True
# str2 = "What's up, Doc?"  # False

# print(str1.endswith("!"))
# print(str2.endswith("!"))

'''
Use the endswith method to determine what a string ends with. In this case, 
an exclamation mark. 
'''
# ---

'''
3. Starting with the string:
famous_words = "seven years ago..."

Show two different ways to create a new string with "Four score and " 
prepended to the front of the string referenced by famous_words.
'''

# famous_words = "seven years ago..."
# prepended_words = "Four score and "
# print(prepended_words + famous_words)

# print(f"{prepended_words}{famous_words}")

'''
The strings can be concatenated directly, or string interpolation can be 
used to ensure the strings are printed together.
'''
# ---

'''
4. Using the following string, print a string that contains the same value, 
but using all lowercase letters except for the first character, which should 
be capitalized.

munsters_description = "the Munsters are CREEPY and Spooky."
# => 'The munsters are creepy and spooky.'
'''

# munsters_description = "the Munsters are CREEPY and Spooky."
# print(munsters_description.capitalize())

'''
One can use the capitalize method to capitalize the first letter of a string.
'''
# ---

'''
5. Starting with the string:
munsters_description = "The Munsters are creepy and spooky."
"tHE mUNSTERS ARE CREEPY AND SPOOKY."

That is, lowercase letters are converted to uppercase, and uppercase letters are converted to lowercase"
'''

# munsters_description = "The Munsters are creepy and spooky."
# print(munsters_description.swapcase())

'''
One can use the swapcase method
'''
# ---

'''
6. Determine whether the name Dino appears in the strings below -- check each string separately:
str1 = "Few things in life are as important as house training your pet dinosaur."
str2 = "Fred and Wilma have a pet dinosaur named Dino."
'''

str1 = "Few things in life are as important as house training your pet dinosaur."
str2 = "Fred and Wilma have a pet dinosaur named Dino."

# print(str1.find("Dino"))
# print(str2.find("Dino"))

# # launch school way
# print("Dino" in str1)
# print("Dino" in str2) 

'''
Launch school way is the way to go, because I think it follows the instructions 
of 'checking each string separately'.
'''
# ---

'''
7. How can we add the family pet, "Dino", to the following list?
flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
'''

# flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
# flintstones.append("Dino")
# print(flintstones)

'''
Use the append method to add an element to a list
'''
# ---

'''
8. In the previous problem, our first answer added 'Dino' to the list like this:
flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
flintstones.append("Dino")

How can we add multiple items to our list (e.g., 'Dino' and 'Hoppy')? Replace the call to append with another method invocation.
'''
# flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
# pets = ["Dino", "Hoppy"]

# flintstones.extend(pets)
# print(flintstones)

'''
One can use the extend method to add multiple objects to an existing list
'''
# ---

'''
9. Print a new version of the sentence given by advice that ends just 
before the word house. Don't worry about spaces or punctuation: remove 
everything starting from the beginning of house to the end of the sentence.

advice = "Few things in life are as important as house training your pet dinosaur."
# Expected output:
# Few things in life are as important as
'''

# advice = "Few things in life are as important as house training your pet dinosaur."
# print(advice[:-33])

# Launch School way
# print(advice.split("house")[0])

'''
Launch schools way is much better, because it doesn't require one to precisely
know which index to remove. You can simply enter the string and the method
does the rest of the work. 
'''
# ---

'''
10. Print the following string with the word important replaced by urgent:
advice = "Few things in life are as important as house training your pet dinosaur."
'''

advice = "Few things in life are as important as house training your pet dinosaur."

advice = advice.replace("important", "urgent")
print(advice)