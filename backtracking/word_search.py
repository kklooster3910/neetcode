"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. 
The same letter cell may not be used more than once.

input  gird[m][n], targetWord string
return boolean 
constraitns:
 sequentially adjacent cells
  same letter cell may not be used more than once
    m >= 2, n >= 2
    len(target) >= 0
   

"""

def wordSearch(grid, target):
    if len(target) == 0: return True
    if len(target) > len(grid) * len(grid[0]): return False

    def backtrack(indexStr, x, y):
        
        if indexStr == len(target) - 1: return True
        directions = [[0, -1],[-1, 0],[0, 1], [1, 0]]
        holder = grid[x][y]
        grid[x][y] = "@"
        for direction in directions:
            nextX, nextY = x + direction[0],y + direction[1]
            if nextX >= 0 and nextX <= len(grid) - 1 and nextY >= 0 and nextY <= len(grid[0]) - 1:
                nextChar = grid[nextX][nextY]
                if nextChar == target[indexStr + 1]:
                    if backtrack(indexStr + 1, nextX, nextY): return True
        grid[x][y] = holder
    
    for i,row in enumerate(grid):
        for i2 in range(len(row)):
            char = grid[i][i2]
            if char == target[0]:
                if backtrack(0,i, i2): return True
    return False

"""
 target = "abc"
    1. find valid starting character
    2. start traversing if and only if at least one of the next possible directions contains the next letter 
    [
        ['@', '@', 'c'],  target = 'abcbcb'
        ['d', 'c', 'b'],
        ['f', 's', 'a'], m x n ** n, mxn  time complexity m X n ^ len(target)?
    ]    
"""
test1 = [
    ['a','b','c'],
    ['a','c','b'],
    ['a','d','a'],
]

test2 = [
    ['c','b','c'],
    ['b','c','b'],
    ['c','b','a'],
]


print(wordSearch(test1, 'abcbcb'))
print(wordSearch(test2, 'abcbcb'))
