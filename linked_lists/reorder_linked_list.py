
"""
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.
input: 1 -> 2 -> 3 -> 4 -> 5
return: 1 -> 5 -> 2 -> 4 -> 3

input: 1 -> 2 -> 3
return: 1 -> 3 -> 2

input: 1 -> 2 -> 3 -> 4 
return: 1 -> 4 -> 2 -> 3

the last node in the list always becomes the next node in line after a re-order -> a reorder consists of moving the last node to the head.next node

lvl - > 5
lvl / 2 = midpoint
midpoint = ciel(lvl / 2) = 3
start = head
start -> node returned from recursiveCall.next
                 
input: 1 -> 2 -> 3 -> 4 -> 5
 1 -> 5 -> 2 -> 3 -> 4
 1 -> 5 -> 2 -> 4 -> 3

1 5 2

1 - 2 - 3 - 4 - 5
1 - 5 - 2 - 3 - 4
1 - 5 - 2 - 4 - 3

1 - 2 - 3 - 4
1 - 4 - 3 - 2

1 - 2 - 3
1 - 3 - 2

list is reordered when the last node is a node that can't be moved

"""

import math

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# def reorderList(head):
#     start = head
#     midPoint = 0

#     def getNodes(node, lvl=1):
#         nonlocal midPoint
#         nonlocal start
#         if node.next is None:
#             midPoint = math.ceil(lvl / 2)
#             return node
#         lastNode = getNodes(node.next, lvl+1)
#         if lvl >= midPoint: 
#             nextNode = start.next
#             start.next = lastNode
#             lastNode.next = nextNode
#             start = nextNode
#             return node
#         else: return

#     getNodes(head)
#     start.next = None
#     return head

# input: 1 -> 2 -> 3 -> 4 -> 5
# return: 1 -> 5 -> 2 -> 4 -> 3

def reorderList(head):
    start = head
    mid = 0

    def reorder(node, lvl=1):
        nonlocal start
        nonlocal mid
        if node.next is None:
            mid = math.ceil(lvl / 2)
            return node
        lastNode = reorder(node.next, lvl+1)
        if lvl >= mid:
            nextNode = start.next
            start.next = lastNode
            lastNode.next = nextNode
            start = nextNode
            return node
        else: return 
    reorder(head)
    start.next = None
    # return here for testing
    # return head


a = [1, 2, 3, 4]
# b = [1, 3, 4, 7, 8, 9]
node = ListNode(a[0])
# node2 = ListNode(b[0])
list1 = node 
# list2 = node2
for i in range(1,len(a)):
    val = a[i]
    # val2 = b[i]
    newNode = ListNode(val)
    # newNode2 = ListNode(val2)
    node.next = newNode
    node = newNode
    # node2.next = newNode2
    # node2 = newNode2
 
# for i in range(1,len(b)):
#     # val = a[i]
#     val2 = b[i]
#     # newNode = ListNode(val)
#     newNode2 = ListNode(val2)
#     # node.next = newNode
#     # node = newNode
#     node2.next = newNode2
#     node2 = newNode2
 

def printAllNodes(node):
    while node :
        print(node.val)
        node = node.next

print(printAllNodes(reorderList(list1)))
# print(math.ceil(5 / 2))