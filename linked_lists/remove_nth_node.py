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

# input is going to be head: ll node, n -> which is the number from the last node indicating which node we want to remove
# return head 
# head can be none
# can only get one node passed in
# 1 <= n <= linklist.size() if linklist is not None
# node to remove = ll.size() - n + 1
# use two counter
# first: 1 second: 1
# nodeToRemove = 0 
# currentNode = head
# while cN:
#   iterate to end of ll, incremenet first counter on each node
#   nodeTOremove = first - n + 1
#   if second == 1:
#       currentNode = head
#   loop through again incrementing second and when second == nodeToRemove:
# when looping through second time, need previous node to set prevNode.next = currentNode.next

# 1 -> 2 -> 3 -> 4 -> 5
# 1 -> 2 -> 3 -> 5
from utils import LinkedList

def removeNthTwoPass(head, n):
    nodeToRemove = 0
    firstCount = 0
    secondCount = 0
    currentNode = head

    while currentNode:
        firstCount += 1
        if currentNode.next is None:
            nodeToRemove = firstCount - n + 1
            break
        currentNode = currentNode.next

    currentNode = head
    prevNode = None
    while currentNode:
        secondCount += 1
        if secondCount == nodeToRemove:
            if nodeToRemove == 1:
                head = currentNode.next
            else:
                prevNode.next = currentNode.next
        prevNode = currentNode
        currentNode = currentNode.next

    return head 

list1 = LinkedList(4, True)
LinkedList.printList(list1)
removed1 = removeNthTwoPass(list1.head, 3)
LinkedList.printNodes(removed1)