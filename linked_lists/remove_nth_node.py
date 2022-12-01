"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

"""

# input = node: head, n: 2 -> remove the third to last node
# return the head node

"""
n - 2
h                   t
1 -> 2 -> 3 -> 4 -> 5
1 -> 2 -> 3 -> 5
calculate at base case numOfCalls = 5 - n + 1 => at lvl 4 I need to remove that node

implement a recursive fn that takes h, n, lvl -> # of recursive calls
    base case is when there is no next node:
        set var to determine the lvl on where I want to remove the node: lvl - n + 1 = 5 - 2 + 1: remove node at lvl 4
        also going to return node
    have last node returned:
        if I'm at lvl I need to remove:
            do removing and relinking logic
            if I'm at lvl 4 and I want to remove that node
            instead of returning the node which lvl I'm on, I'll return the 5 node
        else:
            return node
    return head
"""

# 1 -> 2 -> 3 -> 4 -> 5
# n -> remove the 4 node

def removeNthNode(head, n):
    if head is None: return None
    if head.next is None: return None

    lvlToRemove = 0
    # lvlToRemove = 4
    def removeNode(node, n, lvl = 1):
        nonlocal lvlToRemove
        if node.next is None:
            lvlToRemove = lvl - n + 1
            return node
        lastNode = removeNode(node.next, n, lvl + 1)
        # handle removing last node
        if lvl + 1 == lvlToRemove:
            node.next = None
            return 
        # handle removing any other node
        if lvlToRemove == lvl:
            return lastNode
        elif lvlToRemove - 1 == lvl:
            node.next = lastNode
        else: return
    removeNode(head, n)
    # handle removing first node
    if lvlToRemove == 1:
        head = head.next
    return head

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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
removed1 = removeNth

def printAllNodes(node):
    while node :
        print(node.val)
        node = node.next

printAllNodes(removeNthNode(list1, 4))