class Node :

    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:

    def __init__(self):
        self.head = None
    def insertdata(self,data):
        newnode = Node(data)
        if self.head == None:
            self.head = newnode
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = newnode

    def deleteAtEnd(self):
        
        
        if self.head is None:
            print("List is Already Empty ")
        if self.head.next is None:
            self.head = None
        
        current = self.head
        prev = None
        while current is not None:
                prev = current
                current = current.next
        prev.next = None
        
        print("Node Is Deleted ")
    
    def printList(self):
        if self.head is None:
            print("No Element is List")
        else:
            current = self.head
            while current is not None:
                print(current.data,end=' ')
                current = current.next

my_list = LinkedList()

while True:
    print()
    print(" choose an valid option For Linked List: ")
   
    print('''
    1)  Insert data
    2)  Delete Node At End
    3)  print data
    4)  Exit
    ''')
    try:
       option=int(input("enter your choice  "))
       print()
    except:
       print("please enter valid option  ")
    if option == 1:
           my_list.insertdata(int(input("Enter the data : "))) 
    elif option == 2:
        my_list.deleteAtEnd()
    elif option == 3:
        my_list.printList()  # Output: 10 -> 20 -> 30 
    elif option == 4:
        exit()
                        