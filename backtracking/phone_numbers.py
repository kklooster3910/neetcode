"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations 
that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) 
is given below. Note that 1 does not map to any letters.

"""

#inputOne = str  "2345"
#inputTwo = str  "23"
#1: 
#2: abc
#3: def
#4: ghi
#5: jkl
#6: mno
#7: pqrs
#8: tuv
#9: wxyz
#0: _
#*: +
##: ^

# ['ad', 'bd', 'cd', 'be', 'bf', 'ce', 'cf']



# def phoneNums(str): # input is "23"
#     combos = []

#     possibleChars = { 
#         '2': 'abc',
#         '3': 'def',
#         '4': 'ghi',
#         '5': 'jkl',
#         '6': 'mno',
#         '7': 'pqrs',
#         '8': 'tuv',
#         '9': 'wxyz'
#     }
    
#     def backtracking(combo=[], idx=0, lvl=0):
#         print('top of fn', combos)
#         if len(combo) == len(str):
#             combos.append(''.join(combo))
#         else:
#             # nextChars = possibleChars[str[idx]].split('') # [a,b,c]
#             # nextChars = list(possibleChars[str[idx]]) # [a,b,c]
#             nextChars = possibleChars[str[idx]] # [a,b,c]
            
#             print('before for loop')
#             print(nextChars)

#             for char in nextChars:  # [a,b,c]
#                 print('inside for loop')
#                 print(char, lvl, idx)
#                 combo.append(char) 
#                 print('after combo append')
#                 print(combo, lvl, idx)
#                 backtracking(combo, idx+1, lvl+1) # ['a'], 1
#                 combo.pop()
#                 print('after pop')
#                 print(combo, lvl, idx)
#             # for i in range(len(nextChars)):
#             #     combo.append(nextChars[i])
#             #     backtracking(combo, idx+1)
#             #     combo.pop()
#     backtracking()
#     return combos

# print(phoneNums('23'))
# print(phoneNums('234'))

#S1 L1: idx 0, combo = "" => creates frame for 'a'  *eventually 'b' & 'c'

#S2 L2: idx 1, combo = "a" => creates frames for 'ad'  *eventually 'ae' & 'af'

#S3 L3: idx 2, combo = 'ad' => adds to combos and return

#S4 L2 idx 1, combo = 'ad' => pop and create frame for 'ae'

#S5 L3: idx 2, combo = 'ae' => adds to combos and return

#S6 L2 idx 1, combo = 'ae' => pop and create frame for 'af'

#S7 L3: idx 2, combo = 'af' => adds to combos and return

#S8 L2 idx 1, combo = 'af' => pop and return

#S9 L1: idx 1, combo = "a" => pop and return

#S10 L1: idx 0, combo = "" => creates frame for 'b'  *eventually 'c'

#S L2: idx 1, combo = "b" => creates frames for 'bd' & 'be' & 'bf'

#S L2: idx 1, combo = "c" => creates frames for 'cd' & 'ce' & 'cf'

