''' Inserting an Element to a Pos In singly LinkedList

It Takes O(n) time complexity to Insert the element '''

class Node :

    def __init__(self,data) -> None:
        self.data = data
        self.next = None
    
class LinkedList:

    def __init__(self) -> None:

        # here head will point to the first node of Linked List
        self.head = None

    # Inserting data to Linked List
    def insertAtPostion(self,data,pos):
        
        newnode = Node(data) # Creating Object Of Node class
        if pos == 1:
            newnode = self.head
            self.head = newnode
           
            
        else:
            count = 1
            previ = None
            current = self.head
            while(current != None and count < pos):
                previ = current
                current = current.next
                count +=1
            if count < pos:
                    print("Invalid position.")
                    return

            newnode.next = current
            previ.next = newnode
            print("{} Inserted At {} position : ".format(data,pos))
    
    
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
    1)  Insert data At any Postion
    2)  print data
    3)  Exit
    ''')
    try:
       option=int(input("enter your choice  "))
       print()
    except:
       print("please enter valid option  ")
    if option == 1:
           my_list.insertAtPostion(int(input("Enter the data : ")),int(input("Enter the Postion : "))) 
    elif option == 2:
        my_list.printList()  
    
    elif option == 3:
        exit()
                        