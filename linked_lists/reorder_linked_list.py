
"""
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.
"""

#input: 7 > 4 > 2 > 9 > 1 > 6

#Input:  1 > 2 > 3 > 4 > 5 > 6 > 7 > 8 > 9

#Output: 1 > 9 > 2 > 8 > 3 > 7 > 4 > 6 > 5

#Input:  1 > 2 > 3 > 4 > 5

#Output 1 > 5 > 2 > 4 > 3


"""
    Naive:
        Start w/ head [1]
    
    Iterative:
        Grab all nodes in a list, in order
        Iterate across nodes grabbing ith and last element - i node

        Have an array of all nodes
            Resort - change connections
                if (!array[i+1]) break;
                first starts at index i node
                last is last node in array
                    last = array[array.length - i]
                        or pop

                next = first.next #2
                first.next = last #1 > 5
                last.next = next    #  1 > 5 > 2
                    #1 > 5 > 2 > 4 > 3

                array.pop()


                next = first.next > 

                                            First = first element of arr  => 1
                    Last = last element of array => 4
                next.next = last     => 3 > 4
                
                Last.next = next  => 1 > 5 > 2

                first = next => 2
                array.pop() => remove 5 => 1,2,3,4


        
"""

# def reOrder(head):
#     array = [head]
#     current = head

#     while current:
#         array.append(current)
#         current = current.next
#     # print(array)

#     for i in range(0, len(array)):
#         if i + 1 > len(array): 
#             break

#         first = array[i]
#         last = array[len(array) - 1]

#         next = first.next
#         first.next = last
#         last.next = next
        
#         # print(array)
#         # for i in range(0, len(array)):
#         #     print(array[i].val)
#         array.pop()

#     return head
import math

# def reorderList(head):
#     if head is None: return None
#     if head.next is None: return head

#     start = head
#     mid = 0

#     def reorder(node, lvl=1):
#         nonlocal start
#         nonlocal mid
#         if node.next is None:
#             mid = math.ceil(lvl / 2)
#             return node
#         lastNode = reorder(node.next, lvl+1)
#         if lvl >= mid:
#             nextNode = start.next
#             start.next = lastNode
#             lastNode.next = nextNode
#             start = nextNode
#             return node
#         else: return

#     reorder(head)
#     start.next = None
#     return head
    
# 1 - 2 - 3 - 4 - 5
# 1 - 2 - 3 - 4

def reorder(head):
    # currentNode = head
    slow = head
    fast = head


    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    currentNode = slow
    prevNode = None
    while currentNode: #4
        nextNode = currentNode.next #5
        currentNode.next = prevNode #4.next = 5
        prevNode = currentNode # 3
        currentNode = nextNode # 4
    
    first = head # 1 > 2 > 3
    second = prevNode # 5 > 4 > 3

    while second.next:
        nextNode = first.next
        first.next = second
        first = nextNode # 5
        secondNext = second.next
        second.next = first
        second = secondNext

    return head

from utils import LinkedList
list1 = LinkedList(5)
# LinkedList.printList(list1)
reorder = reorder(list1.head)
LinkedList.printNodes(reorder)
