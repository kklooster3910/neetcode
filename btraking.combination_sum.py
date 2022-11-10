"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. 

You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.


"""

# input arr: [1, 2, 4, 6, 19, 3, 7, 74, 1005] target: 25

# return [[19, 6], [6, 4, 7, 3, 4, 1], [6, 6, 6, 6, 1], [4, 4, 4, 4, 4, 4, 1]] -- possible return example
#        25
#        / \
#       19  7
#       /   \
#      6     6

# recursion - first thing is a base case
#   [6, 2, 4, 1, 19, 3, 7, 74, 1005]
"""
review the Time Complexity on leetcode! -> you'll need to spend some time with this solution, draw it out and diagram it how they have in the solution

figure out how to work into the code if you should continue with the iteration, if you're solution is worth working towards --> will cost computational power

"""

inputArry = [3, 4, 5]
# target - 8

def combinationSums(arr, target):
    returnArr = []
    #returnArr = [[3, 5], [4, 4]]

    def backtrack(startIdx, currentSum, currentComb):
        if target < currentSum:
            return
        if target == currentSum:
            returnArr.append(currentComb)
            return
        # target - 8 
        # 2, 5, [5]
        for i in range(startIdx, len(arr)):
            nextSum = currentSum + arr[i]
            # 5 + 5
            if  nextSum == target:
                returnArr.append(currentComb + [arr[i]])
                continue
            if target < nextSum:
                continue
            backtrack(i, nextSum, currentComb + [arr[i]])


    for i in range(len(arr)):
        # [3, 4, 5]
        backtrack(i, arr[i], [arr[i]])

    return returnArr

print(combinationSums(inputArry, 8))