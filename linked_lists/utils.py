class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def createLL(length):
        

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
