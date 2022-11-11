"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

"""

def generateParens(pairs): #3
    combos = []

    def backtrackParens(combo=[], left=0, right=0, level=0):
        nextLevel = level + 1
        print('level=',nextLevel)

        print(left, right, combo)
        if len(combo) == pairs * 2:
            print('appending and returning')
            combos.append("".join(combo))
        #   return
        if left < pairs:
            print('inside Left < pairs, going down left')
            combo.append('(')
            backtrackParens(combo, left+1 , right, nextLevel)
            combo.pop()
            print('backout of left, level=',nextLevel)
            print(left, right, combo)

        if right < left:
            print('inside right < pairs, going down right')
            combo.append(')')
            backtrackParens(combo, left , right+1, nextLevel)
            combo.pop()
            print('backout of right, level=',nextLevel)
            print(left, right, combo)

    backtrackParens()
    return combos
  



print(generateParens(3))
# n = 2
# generateParens
# step 1 level 1
#  [] left 0 right 0 => call left
# step 2 level 2
#  ['(']    left 1 right 0 => call left
# step 3 level 3
#  ['(', '('] left 2 right 0 => call right
# step 4 level 4
#  ['(', '(', ')'] left 2 right 1 => call right
# step 5 level 5
# ['(', '(', ')', ')'] left 2 right 2  => call right 
# step 6 level 6 
# ['(', '(', ')', ')']
# append and return => go back up
# step 7 level 5
# ['(', '(', ')', ')']
# no more options, pop and return
# step 8 level 4
# ['(', '(', ')']
# no more options, pop and return
# step 9 level 3
# ['(', '(']
# no more options, pop and return
# step 10 level 2
# ['('] left 1 right 0 => call right
# step 11 level 3
# ['(', ')' ] left 1 right 1 => call left
# step 12 level 4
# ['(', ')', '('] left 2, right 1 => call right
# step 13 level 5
# ['(', ')', '(', ')]append then return
# pop ['(', ')', '(']
# pop ['(', ')']
# pop ['(']
# pop []

"""
level= 1
0 0 []
inside Left < pairs
level= 2
1 0 ['(']
inside Left < pairs
level= 3
2 0 ['(', '(']
inside right < pairs
level= 4
2 1 ['(', '(', ')']
inside right < pairs
level= 5
2 2 ['(', '(', ')', ')']
backout of right, level= 4
2 1 ['(', '(', ')']
backout of right, level= 3
2 0 ['(', '(']
backout of left, level= 2
1 0 ['(']
inside right < pairs
level= 3
1 1 ['(', ')']
inside Left < pairs
level= 4
2 1 ['(', ')', '(']
inside right < pairs
level= 5
2 2 ['(', ')', '(', ')']
backout of right, level= 4
2 1 ['(', ')', '(']
backout of left, level= 3
1 1 ['(', ')']
backout of right, level= 2
1 0 ['(']
backout of left, level= 1
0 0 []
['(']

"""