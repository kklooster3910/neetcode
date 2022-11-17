"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

             3
            / \
            4    6
          /  \    /\
          5   7  7   8
                     \
                      0

          3 --> { value: 3, children: { left: {}, right: {} } } 
          node {
            left : node | null,
            right: node | null 
            val: someval
          }

        check if root  node has a value and return 0 if None
        3 -> depth = 1
        pass in depth + 1
        return depth 3 up the call stack and return
        
"""

def maximumDepth(root, depth = 0):
    if root.value == None:
        return depth
    leftDepth = maximumDepth(root.left, depth + 1)
    rightDepth = maximumDepth(root.right, depth + 1)
    if leftDepth > rightDepth:
        return leftDepth
    else:
        return rightDepth

""""
1st lvl: root: 3, depth: 0 => Go Left
2nd lvl: left: root: 4, depth: 1 => Go Left
3rd lvl: left: root: 5, depth: 2 => Go Left
4th lvl: root: null => return 3 
3rd lvl: left: root: 5, depth: 2 => Go Right
4th lvl: root: null => return 3 
3rd lv: root 5 => compare 3 | 3 => return 3

2nd lvl: left: root: 4, depth: 1 => go right
3rd lvl: root: 7, depth 2 => go left
4th lvl: Root: null > return 3
3rd lvl: root: 7, depth 2 => go right
4th lvl: Root: null > return 3
3rd lvl: root: 7 => compare 3 | 3 => return 3
2nd lvl: root: 4, return 3 | 3 => 3

1st lvl: root: 3, depth: 0 => Go Right
...
""""