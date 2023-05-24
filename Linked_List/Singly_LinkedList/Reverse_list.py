class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList :

    def __init__(self) -> None:
        self.head = None
    
    def insertData(self,data):
        newnode  = Node(data)
        if self.head is None:
            self.head = newnode  
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = newnode
    
    def reverseList(self):
        stack = []
        current = self.head
        while current is not None:
            stack.append(current.data)
            current = current.next
            
        # putting the element reversly to the LinkedList
        current = self.head
        while current is not None:
            current.data = stack.pop()
            current = current.next
        # self.printList()
        
    
    def printList(self):
        if self.head == None:
            print("List Is Empty ")
        else:    
            current = self.head
            while current != None:
                print(current.data,end='-->')
                current = current.next
            print("None")
my_list = LinkedList()

while True:
    print()
    print(" choose an valid option For Linked List: ")
   
    print('''
    1)  Insert data
    2)  Reverse List
    3)  print data
    4)  Exit
    ''')
    try:
       option=int(input("enter your choice  "))
       print()
    except:
       print("please enter valid option  ")
    if option == 1:
           my_list.insertData(int(input("Enter the data : "))) 
    elif option == 2:
        my_list.reverseList()
    elif option == 3:
        my_list.printList()  
    elif option == 4:
        exit()
                                