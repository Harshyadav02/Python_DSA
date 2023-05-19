''' A represntation of Singly List '''

class Node :

    def __init__(self,data) -> None:
        self.data = data
        self.next = None
    
class LinkedList:

    def __init__(self) -> None:

        # here head will point to the first node of Linled List
        self.head = None

    # Inserting data to Linked List
    def insertdata(self,data):
        newnode = Node(data)
        if self.head == None:
            self.head = newnode
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = newnode
    
    # Printing data to the List
    def printList(self):
        current = self.head
        while current != None:
            print(current.data,end=' ')
            current = current.next
# Creating an object linked list
my_list = LinkedList()

while True:
    print()
    print("press choose an valid option For Linked List: ")
   
    print('''
    1)  Insert data
    2)  print data
    3)  Exit
    ''')
    try:
       option=int(input("enter your choice  "))
       print()
    except:
       print("please enter valid option  ")
    if option == 1:
           my_list.insertdata(int(input("Enter the data"))) 
    elif option == 2:
        my_list.printList()  # Output: 10 -> 20 -> 30 
    elif option == 3:
        exit()
                        