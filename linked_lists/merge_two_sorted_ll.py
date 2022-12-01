"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

node = {
    value: 1
    next: { ...node }
}

list one -> 1 - 2 - 5 
list two -> 2 - 3 - 6 


1 2 3 4 

return -> 1 - 2 - 3 - 4 - 5 - 6 - 7 - 8

l1 = 1, 4
l2 = 3, 5

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# list1 or list2 head node value is null, if that is the case, just return the valid list and be done
# if whatever node I'm looking at it is null I've reached the end of whatever particular list
# compare list1 and list2 head self.value and set the appropriate next value

# recursive processing --> look these up
# pre order
# in order666666
# post order


# dosomething
# dosomething
# recur


# iterative solution -> 
# TODO: Do recursive solution for this

# def mergeLinkedList(head1, head2):

#     """
#         l1  -> 
#     """
#     if head1 is None and head2 is None:
#         return dummy
        
#     if head1 is None:
#         return head2
#     if head2 is None:
#         return head1

#     dummy = ListNode()

#     tail = dummy
#     while head1 and head2:
#         if head1.value >= head2.value:
#             tail.next = head2
#             head2 = head2.next
#         else:
#             tail.next = head1
#             head1 = head1.next
#         tail = tail.next

#     if head1 is None:
#         tail.next = head2
#     if head2 is None:
#         tail.next = head1

#     # [0,1,1,1,2,3,4,5,6,]
#     return dummy.next

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



# def mergeLLRecursive(head1, head2):
#     if head1 and head1 is None: return None
#     if head1 is None: return head2
#     elif head2 is None: return head1

#     if head1.val <= head2.val:
#         head1.next = mergeLLRecursive(head1.next, head2)
#         print(head1.val)
#         return head1
#     else:
#         head2.next = mergeLLRecursive(head1, head2.next)
#         print(head2.val)
#         return head2


# list one -> 1 - 2 - 5 
# list two -> 2 - 3 - 6 
# head -> None -> 1
# a = [1,5,7,7,10,11]
# b = [2,6,7, 8, 9]
# head -> 1 - 2 - 5 -6 - 7 - 7 - 8 - 9 - 10
# def mergeTwoLinkedListsI(head1, head2):
#     if head1 is None and head2 is None:
#         return None
#     if head1 is None:
#         return head2
#     if head2 is None:
#         return head1
    
#     dummy = ListNode()
#     head = dummy
#     while head1 and head2:
#         if head1.val <= head2.val:
#             head.next = head1
#             head1 = head1.next
#         else:
#             head.next = head2
#             head2 = head2.next
#         head = head.next
    
#     if head1:
#         head.next = head1
#     if head2:
#         head.next = head2
#     return dummy.next


# list one -> 1 - 3 
# list two -> 2 - 4
def mergeTwoLinkedListsR(head1, head2, lvl = 0):
    if head1 is None and head2 is None:
        return None
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    
    if head1.val < head2.val:
        node = mergeTwoLinkedListsR(head1.next, head2, lvl + 1)
        head1.next = node
        return head1
    else:
        node = mergeTwoLinkedListsR(head1, head2.next, lvl + 1)
        head2.next = node
        return head2

# frame 1 -> head1: 1 head2: 2
# frame 2 -> head1: 2, head2: 2 --> node = head2 head1 -> 1 - 2 - 2
    
# list one -> 1 - 5 - 7
# list two -> 2 - 6 - 8
# head1 = ListNode(1)
# head1.next = ListNode(5)

# a = [1,5, 10, 11]
# b = [2,6,7, 7, 8, 9]

# list one -> 1 - 5 - 7
# list two -> 2 - 6 - 8
def mergeTwoLinkedListsI(head1, head2):
    if head1 is None and head2 is None: return None
    if head1 is None: return head2
    if head2 is None: return head1
    dummy = ListNode()
    head = dummy
    while head1 and head2:
        if head1.val < head2.val:
            head.next = head1
            head1 = head1.next
        else:
            head.next = head2
            head2 = head2.next
        head = head.next
    if head1: head.next = head1
    if head2: head.next = head2
    return dummy.next

def mergeTwoLinkedListsR(head1, head2):
    if head1 is None and head2 is None: return None
    if head1 is None: return head2
    if head2 is None: return head1

    if head1.val < head2.val:
        node = mergeTwoLinkedListsR(head1.next, head2)
        head1.next = node
        return node
    else:
        node = mergeTwoLinkedListsR(head1, head2.next)
        head2.next = node
        return node


a = [1, 2, 3]
b = [1, 3, 4, 7, 8, 9]
node = ListNode(a[0])
node2 = ListNode(b[0])
list1 = node 
list2 = node2
for i in range(1,len(a)):
    val = a[i]
    # val2 = b[i]
    newNode = ListNode(val)
    # newNode2 = ListNode(val2)
    node.next = newNode
    node = newNode
    # node2.next = newNode2
    # node2 = newNode2
 
for i in range(1,len(b)):
    # val = a[i]
    val2 = b[i]
    # newNode = ListNode(val)
    newNode2 = ListNode(val2)
    # node.next = newNode
    # node = newNode
    node2.next = newNode2
    node2 = newNode2
 

def printAllNodes(node):
    while node :
        print(node.val)
        node = node.next

# printAllNodes(list1)
# printAllNodes(list2)

"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

list one -> 1 - 2 - 5 
list two -> 2 - 3 - 6 

constraints:
objectives:
therefore:

optional solutions: eg: recursion, iterative, data structures

necessity: what do we need to solve this

go over solutions -> explain logic of solution
"""


    
mergedList = mergeTwoLinkedListsI(list1, list2)
printAllNodes(mergedList)