''' Inserting an Element to end In singly LinkedList

It Takes O(n) time complexity to Insert the element '''

class Node :

    def __init__(self,data) -> None:
        self.data = data
        self.next = None
    
class LinkedList:

    def __init__(self) -> None:

        # here head will point to the first node of Linled List
        self.head = None

    # Inserting data to Linked List
    def insertAtEnd(self,data):
        newnode = Node(data) # Creating Object Of Node class
        if self.head == None:
            self.head = newnode
        else:
            current_node = self.head
            while current_node.next != None:
                current_node = current_node.next 
            current_node.next = newnode
        print("Element Inserted At End ")
    
    
    # Printing data to the List
    def printList(self):
        if self.head == None:
            print("List Is Empty ")
        else:    
            current_node = self.head 
            while current_node != None:
                print(current_node.data,end='-->')
                current_node = current_node.next
            print("None")
# Creating an object linked list
my_list = LinkedList()

while True:
    print()
    print(" choose an valid option For Linked List: ")
   
    print('''
    1)  Insert data At End
    2)  print data
    3)  Exit
    ''')
    try:
       option=int(input("enter your choice  "))
       print()
    except:
       print("please enter valid option  ")
    if option == 1:
           my_list.insertAtEnd(int(input("Enter the data : "))) 
    elif option == 2:
        my_list.printList()  
    
    elif option == 3:
        exit()
                        