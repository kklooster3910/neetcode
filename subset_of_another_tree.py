"""
Given the roots of two binary trees, root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
()
A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.
 root = [3,4,5,1,2,6,7], subRoot = [4,1,2]
 root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]

            3                   4
        4       5           1       2
      1   2               0  7
     0 7  

           3                   4
      4       5            1       2
    1    2   
        0
"""
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Iterative steps -> Queue, BFS-ish
#  ITerating until:
#   Current nodes starting point must be the same as the subRoot
#   Call recursive function with current node
#  Is currents.left and currents right both equal to subRoots left and right
#   Recursively check if current.left === recursive check if subRoot.left

from collections import deque

def subsetOfAnotherTree(node, subrootNode):
  queue = deque([])

  while (len)