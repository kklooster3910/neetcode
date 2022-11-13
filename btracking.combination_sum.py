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
inputArry2 = [1, 3, 4, 5]
inputArry3 = [2,3,6,7]
inputArry4 = [4,2,8]
# target - 8

# def combinationSums(arr, target):
#     returnArr = []
#     #returnArr = [[3, 5], [4, 4]]

#     def backtrack(startIdx, currentSum, currentComb):
#         if target < currentSum:
#             return
#         if target == currentSum:
#             returnArr.append(currentComb)
#             return
#         # target - 8 
#         # 2, 5, [5]
#         for i in range(startIdx, len(arr)):
#             nextSum = currentSum + arr[i]
#             # 5 + 5
#             if  nextSum == target:
#                 returnArr.append(currentComb + [arr[i]])
#                 continue
#             if target < nextSum:
#                 continue
#             backtrack(i, nextSum, currentComb + [arr[i]])
#             # this solution doesn't quite fulfill all standards of backtracking since it doesn't pop something off the array?
#             # leetcode solution is cleaner

#     for i in range(len(arr)):
#         # [3, 4, 5]
#         backtrack(i, arr[i], [arr[i]])

#     return returnArr

def combinationSums(arr, target):
    allCombos = []

    def backtracking(idx, currentSum, currentCombo, lvl = 0):
        print('top of recursive fn', idx, currentSum, currentCombo, lvl)
        if target == currentSum:
            # make a deep dupe of combo to append to all combos or else currentCombo will be constantly mutated
            print('target = currentSum condition')
            print(idx, currentSum, currentCombo, lvl)
            allCombos.append(list(currentCombo))
            return
        if currentSum > target:
            return
        for i in range(idx, len(arr)):
            currentCombo.append(arr[i])
            # give the current num as many chances as it needs to sum to target before moving on
            print(' in loop before recursive call')
            print(idx, currentSum, currentCombo, lvl)
            backtracking(i, currentSum + arr[i], currentCombo, lvl+1)
            # backtrack and pop off last number from currentCombo
            print('before pop', currentCombo)
            currentCombo.pop()
            print('after pop', currentCombo)

    for i in range(0, len(arr)):
        backtracking(i, arr[i], [arr[i]])

    return allCombos

# inputArry = [3, 4, 5]
print(combinationSums(inputArry, 8))
# print(combinationSums(inputArry2, 8))
# print(combinationSums(inputArry3, 7))
# print(combinationSums(inputArry4, 8))