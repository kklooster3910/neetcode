"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

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
# stack --> [] first in last out
# ['(', '[', '{', '(']
# '}' -> return false
# if I get to the end of the string and haven't returned false, return true
# edge case if len of string is odd return false
# if len(str) % 2 != 0: return False 


# test1: ([{()()}])

#Create a hash table, with each type of bracket and the value being a count
#Have set with the left & right types of parens respectively
#Keep track of last opening bracket
#Iterate across the input string
  #check if right or left
    #If left, we can simply increment hash at the given paren
      #Last opening bracket becomes current paren
    #If right paren, look up associated left paren in hash table
      #if not a positive integer, the function is false, as we have a closing bracket w/o corr. open bracket
      #if it was positive, decrement value
      #Make sure that last opening bracket is an opening paren to the current closing paren


#At end of string, check hash table, all keys should point to value 0
