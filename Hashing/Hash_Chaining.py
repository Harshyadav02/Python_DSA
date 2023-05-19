'''Chaining is one of the technique to overcome from the collision during hashing
    when collisions happen it store the element in the form form of chain 
    
    for example ---> a element is stored on the zeroth index of the list 
    now another element's address came on the same address as the first element
    here the element get collide  so the element will get stored to next

    [[1] [2] [3] [4] [5]]
    now a new element got the address 1 but to is already in the list so the element will be stored
    next to it 
    [[1] [2,10] [3] [4] [5]]
'''
class Myhash:

    def __init__(self,b) -> None:
        self.bucket = b
        self.table = [[] for x in range(b)]
    def insert(self,x):
        i = x % self.bucket
        self.table[i].append(x)
    def remove(self,x):
        i =x % self.bucket
        self.table[i].remove(x)
    def search(self,x):
        i = x % self.bucket
        return x in self.table[i] 
    def printHash(self):
        print(self.table)
h = Myhash(5) # 5 is the bucket size i.e 5 list will be created inside a list
h.insert(5)
h.insert(1)
h.insert(2)
h.insert(2) # here we get collision
h.insert(3)
h.insert(4)
h.printHash()


