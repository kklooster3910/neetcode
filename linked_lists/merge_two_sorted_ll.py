"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

node = {
    value: 1
    next: { ...node }
}

list one -> 1 - 2 - 3 - 4 - 5 - 7
list two -> 2 - 3 - 6 - 8


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
# in order
# post order


# def mergeAndSort(head1, head2):
#     # l1 = 1, 4
#     # l2 = 3, 5

#     if head1 and head2 is null:
#         return None
#     if head1 is None:
#         # return
#     elif head2 is None:
#         # return 

#     if head1.value > head2.value:
#         head1.next = head2
#         # l1 = 1, 3, 4
#         # l2 = 3, 5
#         mergeAndSort(head1.next, head2.next)
    
#     if head2.value > head1.value: 
#         head1.next = head1
#         # l1 = 1, 3, 4
#         # l2 = 3, 5
#         mergeAndSort(head1.next, head2.next)


dosomething
dosomething
recur

def mergeLinkedList(head1, head2):
    dummy = new ListNode()
    tail = dummy

    while head1 is not None and head2 is not None:
        if head1.value > head2.value:
            tail.next = head1
            head1 = head1.next
        elif head2.value > head.value:
            tail.next = head2
            head2 = head2.next
        tail = tail.next

        if head1 is None:
            tail.next = head2
            return tail
        elif head2 is None:
            tail.next = head1
            return tail
    
