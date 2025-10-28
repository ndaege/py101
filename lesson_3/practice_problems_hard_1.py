'''
1. Will the following functions return the same results?
def first():
    return {
        'prop1': "hi there",
    }

def second():
    return
    {
        'prop1': "hi there",
    }

print(first())
print(second())

No, they will not return the same results. The second function technically has
nothing after the return, so None is returned. 
'''
# ---

'''
2. What does the last line in the following code output?

dictionary = {'first': [1]}
num_list = dictionary['first']
num_list.append(2)

print(num_list)
print(dictionary)

The last line outputs {'first': [1, 2]} because dictionaries are mutable objects. 
'''
# ---

'''
3. Given the following similar sets of code, what will each code snippet print?
one is
two is
three is

A. 
one is ["two"]
two is ["three"]
three is ["two"]

B. 
one is ["two"]
two is ["three"]
three is ["one"]

C. 
one is ["two"]
two is ["three"]
three is ["one"]

Launch School's Answer:
In all three scenarios, the variables one, two, and three inside the mess_with_vars function are local to the function. They are not the same as the variables one, two, and three defined outside the function. This is known as variable shadowing, where the local variables inside the function overshadow the variables outside the function with the same names.
'''

'''
4. Ben was tasked to write a simple Python function to determine whether an input string is an IP address using 4 dot-separated numbers, e.g., 10.4.5.11.

Alyssa supplied Ben with a function named is_an_ip_number. It determines whether a string is a numeric string between 0 and 255 as required for IP numbers and asked Ben to use it. Here's the code that Ben wrote:
'''

# def is_an_ip_number(str):
#     if str.isdigit():
#         number = int(str)
#         return 0 <= number <= 255
#     return False

# def is_dot_separated_ip_address(input_string):
#     dot_separated_words = input_string.split(".")
#     if len(dot_separated_words) < 4 or len(dot_separated_words) > 4:
#         return False
#     while len(dot_separated_words) > 0:
#         word = dot_separated_words.pop()
        
#         if is_an_ip_number(word) is False:
#             return False

#     return True

# print(is_dot_separated_ip_address("0.0.255.0"))

'''
Alyssa reviewed Ben's code and said, "It's a good start, but you missed a few things. You're not returning a false condition, and you're not handling the case when the input string has more or less than 4 components, e.g., 4.5.5 or 1.2.3.4.5: both those values should be invalid."

Help Ben fix his code.
'''

'''
Launch School's Answer
def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")
    if len(dot_separated_words) != 4:
        return False

    while dot_separated_words:
        word = dot_separated_words.pop()
        if not is_an_ip_number(word):
            return False

    return True
'''
# ---

'''
5. What do you expect to happen when the greeting variable is referenced in the last line of the code below?
'''

# if False:
#     greeting = "hello world"

# print(greeting)

'''
The code results in an error, because greeting does not exist in the global scope.
'''