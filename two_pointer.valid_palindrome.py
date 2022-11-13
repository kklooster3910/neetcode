"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

"""
# input string - 'racecar'
# return true if all characters are the same in reverse - can include numbers

# input race#car 

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# convert all the characters to lowercase, remove non aphanumeric chars and then reverse string and compare to input O(2n) time O(1) space
# two pointers start and an end pointer and then we compare start pointer to end pointer and if they're different return false, and if they're the same then we increment start and decrement end and continue comparing
# initialize var isPalindrome = true, while true do comparisons -> know we've reached end when start == end, return true O(n) time O(1) space
# isalnum():

# "A man, a plan, a canal: Panama"
# def isPalindrome(str):
#     start = 0 
#     end = len(str) - 1

#     while start < end:
       
#         while start < end and not str[start].isalnum():
#             start += 1
#         while start < end and not str[end].isalnum():
#             end -= 1
            
#         firstChar = str[start]
#         secondChar = str[end]
#         if firstChar.lower() != secondChar.lower():
#             return False
#         start +=1 
#         end -= 1
#     return True 




"""

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

isalnum()

nested loop where we compare every character to every other character in the string and see if it's the same forwards/backwards --> ignoring non alpha numeric characters O(n^2) O(1)
return true if chars same, false if different

O(n) run time and constant space 

create two pointers and iterate from the front and back compare each character that is alpha num

"""

def isPalindrome(str):
    start = 0
    end = len(str) - 1

    while start < end:
        # can't use if here because it will keep going through the rest of the while statement while the while condition will restart loop
        # need to check and make sure start is still less than end here
        while start < end and not str[start].isalnum():
            start += 1
        while start < end and not str[end].isalnum():
            end -= 1
        
        firstChar = str[start]
        lastChar = str[end]
        print(firstChar)
        print(lastChar)
        if firstChar.lower() != lastChar.lower():
            return False
        start += 1
        end -=1
    
    return True


print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))