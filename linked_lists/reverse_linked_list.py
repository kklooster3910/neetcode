"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#Edge cases: node could be null
#Values of each node -5000 to 5000

#Get to the end point with recursive stack calls
# At base case
  # Is no node.next
  # return Node

# Get return value stored from recursive call
  #Set return values next to current node value and return to our parent

#input:
#  5 -> -4000 -> 20 -> 19

#result:
# 19 -> 20 -> -4000 -> 5

# def reverseLinkedList(head):
#     if head is None: return None

#     returningHead = None
#     reverseList(head, returningHead)

#     return returningHead

# def reverseList(node, returningHead):
#     if node.next is None: 
#         returningHead = node
#         return node

#     roleReversal = reverseList(node.next, returningHead) #19

#     roleReversal.next = node

#     return node

  #S1 5 => -4000 => 20 => 19
  #S4 19 => return 19
  #S3 20 => 19.next is 20 and return 

"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Edge cases: node could be null
#Values of each node -5000 to 5000

# def reverseLinkedList(head):
#   """
#     1 -> 2 -> 3

#    constraints:
#     linked list can only move foreward
  
#     objective:
#     reverse these forward facing links in reverse order

#     THERFORE:
#     find a way to have access to the previous node and reconnect the linklist so that they are reversed
    
#     recursive:
#       with recursive solutions we can reach all the way to the end of the recursive call(base case) until we make any logical 
#       decision on how to reconnect them

#       recursion - reaches to the end at returns value 
    
#     necessity:
#       we need access to the previous node before we can re connect the dots

    
#     iterative:
#       ill have to find a way to reconnect as we traverse forward and in the end return the last node
    
#   """

#   def reverse(node):
#       if node.next is None:
#         newHead = node
#         return node

#       nextNode = reverse(node.next)
#       nextNode.next = node

#   if head is None:
#     return None
#   if head.next is None:
#     return head
#   newHead = None

#   reverse(head)

#   return newHead

# def revereseLLIterative(head):
#     """
#     can only traverse LL in one way head - tail

#     need to hold the previous node in memory to reference and set new pointer

#     while loop -> two nodes current node and prev node -> reached end when there is no 
#     if node.next is None then at end and can return that node

#      1 -> 2 -> 3 -> None

#      None < 1 < 2 < 3

#     reconnecting:
#     tempNode -> currentNode
#     currentNode.next -> currentNode

#     traversing: 
#     forward by setting the currentNode -> currentNode.next

#     """
#     prevNode = None #
#     currentNode = head # 1
#     while currentNode:
#         nextNode = currentNode.next # 
#         currentNode.next = prevNode # 
#         prevNode = currentNode #
#         currentNode = nextNode #
    """
    i1 prevNode: None ,currentNode :1, => currentNode.next : None  , links: 1 > None
    i2 prevNode: 1 ,currentNode 2:, => currentNode.next 1:  , links: 2 > 1 > None
    i3 prevNode:2 ,currentNode :3, => currentNode.next :2 , links: 3 > 2 > 1 > None
    finalval: 
    """
    
    # return prevNode

# head1 = ListNode(1)
# head1.next = ListNode(5)

# THIS NEEDS TO BE REVIEWED AND DONE NEXT

a = [1,5,7]
b = [2,6,8]
node = ListNode(a[0])
node2 = ListNode(b[0])
list1 = node 
list2 = node2
for i in range(1,len(a)):
    val = a[i]
    val2 = b[i]
    newNode = ListNode(val)
    newNode2 = ListNode(val2)
    node.next = newNode
    node = newNode
    node2.next = newNode2
    node2 = newNode2
 

def printAllNodes(node):
    while node:
        print(node.val)
        node = node.next
reversed1 = revereseLLIterative(list1)
reversed2 = revereseLLIterative(list2)

printAllNodes(reversed1)
printAllNodes(reversed2)