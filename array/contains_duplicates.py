from collections import defaultdict
"""
    Given an integer array nums, return true if any value appears at least twice in the array, 
    and return false if every element is distinct.

"""
# input []int 

# true if any value appears 2x 
# false if everything is unique

# value could -max to +max

# [3] return false

# [1,2,3,4,5] return false

# [-2, 4, 3, 2, -2] return true 

# current BCR --> a nested loop that compares each integer to every other integer and if ever finding a pair return ture, or false O(n^2) O(1);

testDupe = [1, 2, 3, 5, 6, 2]
testDupe2 = [1, 2, 3, 5, 6]

# { 1: 1, 2: 2, 3: 1 };

# { 1: 1, 2: 2, 3: 1, 5: 1, 6: 1 };

def containsDupes(input):
    # hasDupe = False
    # nums = {}
    
    # for num in input:
    #     if num in nums:
    #         return True
    #     else: nums[num] = 1
    
    # return False
    
    
    # #one line solution - cleaner
    return len(set(input)) != len(input)

    #sol3
    # hashmap = defaultdict(int)
    # for num in input:
    #     if num in hashmap: return True
    #     hashmap[num]+=1
    # return False

print(containsDupes(testDupe))
print(containsDupes(testDupe2))

