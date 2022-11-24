# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. 

Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
"""

# input is going to be a node in a linked list -> could be None -> return None

# 1 -> 2 -> 1 -> 3 -> 5
#                   > 1(head)         
# objective is to detect one cycle -> might have multiple but doesn't matter
# return true if there is a cycle or return false

# objective is to find a cycle somehow -> how to determine there is a cycle 
# visit each node and determine cycle: return true
# otherwise visit every node and if no cycle is found: return false
# two nodes can have the same value

# keep track of how many times I've visited a node

# two pointers fast, slow -> if fast and slow are ever on the same node -> we've hit a cycle and can return true

# Floyds cycle finding algorithm --> Floyd has many algorithms

# Floyd's cycle finding algo
def isCycle(head):
    if head is None or head.next is None:
        return False
    slow = head
    fast = head.next

    # while fast.next:
    while fast:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next
        if fast:
            fast = fast.next
    return False

# hash table solution
def isCycleHash(head):
    if head is None or head.next is None:
        return False
    visitedNodes = {}
    node = head
    while node:
        if node in visitedNodes:
            return True
        else:
            visitedNodes[node]: node
        node = node.next
    return False