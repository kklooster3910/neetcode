"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.


"""
# stack --> [] first in last out
# iterate ([{(})])
# ['(', '[', '{', '(']
# '}' -> return false
# if I get to the end of the string and haven't returned false, return true
# edge case if len of string is odd return false
# def validParenthesis(str):
#     if len(str) % 2 != 0: return False 
#     stack = []

#     for char in str:
#         left = set(['(', '[', '{'])
#         right = {')':'(', '}':'{', ']':'[' }
#         if char in left:
#             stack.append(char)
#         if char in right and stack[len(stack) - 1] != right[char]:
#             return False
#         elif char in right and stack[len(stack) - 1] == right[char]:
#             stack.pop()
    
#     return True
"""
An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.



'([{}()])' input -> return true
{ (: 1, [: 1, {: 1 }

'([{}](' input -> 

contraints:
    - Open brackets must be closed by the same type of brackets.
    - Open brackets must be closed in the correct order. '{[])(}'
    - Every close bracket has a corresponding open bracket of the same type.
"""


# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
input1 = '({[]})'
input2 = '({[]})}'
input3 = '(('

def validParenthesis(str):


print(validParenthesis(input1))
print(validParenthesis(input2))
print(validParenthesis(input3))