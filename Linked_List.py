class Node:
    def __init__(self,key) -> None:
        
        self.key = key
        self.next = None

# Printing the Linked List
def printlist(head):
    curr = head
    while curr != None:
        print(curr.key,end=' ')
        curr = curr.next


head = Node(10)        
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
printlist(head)
