"""

Given an array of meeting time intervals where intervals[i] = [starti, endi],
determine if a person could attend all meetings.

"""
# input [[0, 5], [2, 8], [8, 10]] - > would return false
# input [[3, 5], [9, 10], [0, 2], [6, 7]] - > would return true
# return is a bool - true if you can attend all meetings or false if not

# first BCR -> a nested loop 
# [[0, 5], [2, 8], [8, 10]]
# for loop [0, 5]
    # for loop [2, 8] # return false 
# [[3, 5], [9, 10], [0, 2], [6, 7]]
#  for [3, 5]
#   for [0, 2]

#[[3, 5], [9, 10], [0, 2],[5, 7] [6, 7]]
# sort input O(n*log(n)) -> sort these meeting times in ascending order based on meeting start time
# [[0, 2], [3, 5], [5, 7], [6, 7], [9, 10]]
# two pointers -> start and end
# start: 0, end: len(input) - 1
# while the start is less than the end
# start will be [3, 5] and end [6, 7]

# currentStart, currentEnd    
# for 
# cS = 3, cE = 5
# O(n * log(n)) time  O(1) space
sampOne = [[3, 5], [9, 10], [0, 2], [6, 7], [1, 4]]
sampTwo = [[3, 5], [9, 10], [0, 2], [6, 7]]

# [[0, 2], [3, 5], [6, 7], [9, 10]]
# [[9, 10], [6, 7], [3, 5], [1, 4], [0, 2]]
# !! question --> ASK ABOUT INPUT SIZES eg: do we know the minimal size of this input array? -- could have simplified with edge cases

# [[9, 10], [6, 7], [3, 5], [1, 4], [0, 2]]

def attendAllMeetings(arr):
    if len(arr) <= 1:
        return True

    arr.sort(key=lambda x:x[1], reverse=True)
    currentStart = arr[0][1]
    for i in range(1, len(arr)):
        nextStart, nextEnd = arr[i][0], arr[i][1]
        if currentStart < nextEnd:
            return False
        currentStart = nextStart
    return True



print(attendAllMeetings(sampOne))
print(attendAllMeetings(sampTwo))