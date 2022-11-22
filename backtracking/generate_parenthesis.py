"""

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

"""

def generateParens(pairs): #3
    combo = []
    combinations = []

    def backtracking(left, right):
        if left == right == pairs:
            combinations.append("".join(combo))
            # don't need a return here since other two conditionas won't hit
            return
        if left < pairs:
            combo.append('(')
            backtracking(left + 1, right)
            combo.pop()
        if left > right:
            combo.append(')')
            backtracking(left, right + 1)
            combo.pop()
    
    backtracking(0, 0)
    return combinations
        


print(generateParens(2))
# n = 2
"""
combo : ['(']

left 1 right 0
combo: ['(', '(']

left: 2 right 0
combo: [()]

left 1 right 1
[()(]
left 2 right 1
[]


combinations [(()), ()()]


"""