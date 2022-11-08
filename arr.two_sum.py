"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

# input []nums & target: num
# return array[int] -> indices of the two numbers that add up to the target

# arr: [1, 2, 7, 4, 5, 6, 2] target: 4
# [1, 6] -> [1, 1]: no

# BCR -> nested loop, initialize an empty arr, target: 3
# [1, 2, 7, 4, 5, 6, 2] -> 1 return [1, 6] time O(n^2) space O(1); suboptimal BCR
# O(n); two pointers start: 0 end: len(input)

# 3(target) = 1(current iterating value) + n
# n = 3(target) - 1(curret_iterating_value)
# key = number value = index

# { 1: 0, 2: 1, 7: 2, 4: 3, 5: 4, 6: 5}
# loop through num in input [1, 2, 7, 4, 5, 6] target = 4
# n = target - num

def twoSum(arr, target):
    hashMap = {}
    #sol1
    # for i, num in enumerate(arr):
    #     hashMap[num] = i

    # for i, num in enumerate(arr):
    #     # think about this later - needs to be target - num and not num - target
    #     if target - num in hashMap and i != hashMap[num]:
    #         return [i, hashMap[target - num]]

    # return []

    #sol2
    for i, num in enumerate(arr):
        diff = target - num
        if diff in hashMap:
            return [i, hashMap[diff]]
        hashMap[num] = i
    return []

test = [1, 2, 7, 4, 5, 6]
"""
    { 1: 0, 2: 1, 7: 2, 4: 3, 5: 4, 6: 5}
"""
print(twoSum(test, 4))

#def containsDuplicate(self, nums):