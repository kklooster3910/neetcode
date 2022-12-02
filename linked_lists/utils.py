# from random import randomrange
import random

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, length, isRandom=False):
        self.head = None
        listReference = []
        for i in range(1, length + 1):
            currentNum = 0
            if isRandom:
                currentNum = random.randint(1, length)
            else: currentNum = i
            listReference.append(currentNum)
        self.head = ListNode(listReference[0])
        currentList = self.head
        for i in range(1, len(listReference)):
            val = listReference[i]
            nextNode = ListNode(val)
            currentList.next = nextNode
            currentList = nextNode
    # will print the list given a list
    def printList(self):
        node = self.head
        while node:
            print(node.val)
            node = node.next
    # will print the list given a head node
    def printNodes(node):
         while node:
            print(node.val)
            node = node.next

    # add a remove and add node fn? -> would be good practice
    # remove would remove node at depth passed in, nth removal
    # add would add a node to the end of the list


# list1 = LinkedList(15, True)
# LinkedList.printNodes(list1)