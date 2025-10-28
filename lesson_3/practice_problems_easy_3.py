'''
1. Write two different ways to remove all of the elements from the following 
list:
'''
# numbers = [1, 2, 3, 4]
# numbers.clear()
# while numbers:
#     numbers.pop(0)

# print(numbers)
# ---

'''
2. What will the following code output?
'''
# print([1, 2, 3] + [4, 5])

# [1, 2, 3, 4, 5]
# ---

'''
3. What will the following code output?
'''
# str1 = "hello there"
# str2 = str1
# str2 = "goodbye!"
# print(str1)

# The code will print hello there
# ---

'''
4. What will the following code output?
'''
# my_list1 = [{"first": "value1"}, {"second": "value2"}, 3, 4, 5]
# my_list2 = my_list1.copy()
# my_list2[0]['first'] = 42
# print(my_list1)

# The code will print [{"first": 42"}, {"second": "value2"}, 3, 4, 5], 
# because copy() makes a shallow copy of the list. Since both variables, 
# are not pointing to the same list, the change to the list on one variable
# changes the same object referenced by the other variable. 
# ---

'''
5. The following function unnecessarily uses two return statements to return 
boolean values. Can you rewrite this function so it only has one return 
statement and does not explicitly use either True or False?
'''
def is_color_valid(color):
    # return color == "blue" or color == "green"
    return color in ["blue", "green"]

print(is_color_valid("purple"))