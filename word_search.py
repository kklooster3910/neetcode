"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. 
The same letter cell may not be used more than once.

"""
#input : board => List[List[str]], word => str
"""" target = acdba
[['a', 'b'], 
 ['c', 'd'], => start idx, end idx
 ['d,','e']]
#return: true if contained, else false
"""

# iteratively search for starting points
#  starting points being the first char of the word
# for each starting, want to call recursive function, backtracking algo
# . each recursive call needs to know the origin/start point
# .    the origin would the first value in a reference hash table for visited points
# path [] includes starting point
#  possible directions to move along the path at any given point
#   [[0,1], [1,0], [-1,0], [0,-1]]
# after trying a direction, we will pop the 'path' array to undue that childs changes to the array
# .  this is not strictly necessary but allows us to use a dynamic arrays amortized O(1) push and pop operations
# idea: eeping track of start, backtracking step goes from starts and undues edits based on copy of original array