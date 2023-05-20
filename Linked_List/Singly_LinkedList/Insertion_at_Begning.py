''' Inserting an Element to Begning In singly LinkedList

It Takes O(1) time complexity to Insert the element '''

class Node :

    def __init__(self,data) -> None:
        self.data = data
        self.next = None
    
class LinkedList:

    def __init__(self) -> None:

        # here head will point to the first node of Linled List
        self.head = None

    # Inserting data to Linked List
    def insertAtBegning(self,data):
        newnode = Node(data) # Creating Object Of Node class
        if self.head == None:
            self.head = newnode
        else:
            newnode.next = self.head
            self.head = newnode
        print("Element Inserted At Begining ")
    
    # Printing data to the List
    def printList(self):
        if self.head == None:
            print("List Is Empty ")
        else:    
            current = self.head
            while current != None:
                print(current.data,end=' ')
                current = current.next
# Creating an object linked list
my_list = LinkedList()

while True:
    print()
    print(" choose an valid option For Linked List: ")
   
    print('''
    1)  Insert data At begining
    2)  print data
    3)  Exit
    ''')
    try:
       option=int(input("enter your choice  "))
       print()
    except:
       print("please enter valid option  ")
    if option == 1:
           my_list.insertAtBegning(int(input("Enter the data : "))) 
    elif option == 2:
        my_list.printList()  
    
    elif option == 3:
        exit()
                        