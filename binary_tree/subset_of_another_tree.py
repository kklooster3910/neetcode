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

# from collections import deque

# def compareTrees(node, subNode): #null, null
#     if node is None or subNode is None: return node == subNode
    
#     leftMatch = compareTrees(node.left, subNode.left)
#     rightMatch = compareTrees(node.right, subNode.right)
#     if leftMatch  and  rightMatch : 
#         return True
#     else: 
#         return False
# def subsetOfAnotherTree(node, subrootNode):
#     # functionality = iterates over the nodes until we find a node value that equals to root node of the subrootNode
#     # constraint  - once we find equal values, we gotta be able to validate all of it's children are the same
  
#   queue = deque([node])
#   while (len(queue)):
#     current = queue.leftPop()
#     if (node.val == subrootNode.val):
#         sameTree = compareTrees(node, subrootNode)
#         return sameTree
#     if (current.left): queue.append(current.left)
#     if (current.right): queue.append(current.right)
#   return False