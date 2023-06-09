''' Searching represntation of Singly List

It Takes O(n) time complexity to search the element '''

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
        newnode = Node(data) # Creating Object Of Node class
        if self.head == None:
            self.head = newnode
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = newnode

    # Searching In LinkedList 
    def search(self,key):
        current = self.head
        while current !=None:
            if current.data == key:
                print(key ," is Present")
                break
            else:
                current = current.next
        else:
            print("{} is not present ".format(key))
    # Printing data to the List
    def printList(self):
        if self.head == None:
            print("List Is Empty ")
        else:    
            current = self.head
            while current != None:
                print(current.data,end='-->')
                current = current.next
            print("None")
# Creating an object linked list
my_list = LinkedList()

while True:
    print()
    print(" choose an valid option For Linked List: ")
   
    print('''
    1)  Insert data
    2)  print data
    3)  Search
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
        my_list.printList()  
    elif option == 3:
        my_list.search(int(input("Enter the Key You Wanna Find : ")))
    elif option == 4:
        exit()
                        