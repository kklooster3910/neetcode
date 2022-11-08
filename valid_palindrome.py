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
def isPalindrome(str):
    start = 0 
    end = len(str) - 1
    whileCondition = start < end

    while whileCondition:
       
        while whileCondition and not str[start].isalnum():
            start += 1
        while whileCondition and not str[end].isalnum():
            end -= 1
            
        firstChar = str[start]
        secondChar = str[end]
        if firstChar.lower() != secondChar.lower():
            return False
        start +=1 
        end -= 1
    return True 

print(isPalindrome("A man, a plan, a canal: Panama"))