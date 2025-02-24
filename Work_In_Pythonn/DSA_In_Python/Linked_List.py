'''
singly linked-list := 
A linked list is a list of connected nodes, where each node points to (references) the node in front 

'''
# Creating A Node 
class Node :
    def __init__(self,data):
        self.data=data
        self.next = None #  next is created to point to the next node.
node1 = Node(7)
print(node1.data)
print(node1.next)

# Creating Singly Linked-List Class
class  LinkedList:
    def __init__(self):
        self.head = None 
        print("Vipin")

a = LinkedList() # After Running This What Ever Will Be In LinkeddList They All Will Be Executed.


# Traversal In Single Linked-List
class Node2:
    def __init__(self,data):
        self.data = data
        self.next = None

class  LinkedList1:
    def __init__(self):
        self.head = None
    def traversal(self):
        if self.head is None:
            print("The Linked List is Empty")
        else:
            Temp=self.head
            while Temp is not None:
                print(Temp.data,end="-->")
                Temp = Temp.next
# Insertion Of New Element at beginning.
    def insert_at_beg(self,data):
        print()
        newnode= Node(data) # creating an new node 
        newnode.next = self.head # making an connection between new-node and head-node
        self.head=newnode # changing head to new-node

# Insertion Of New Element at End.
    def insert_at_End(self,data):
        End = Node(data) # created an node.
        Temp2 = self.head # making the head variablle fixed.
        while Temp2.next is  not None: # running an while loop.
            Temp2=Temp2.next # pointing
        Temp2.next=End # connection between last node and  new node.

z=LinkedList1()
n1 = Node(41)
z.head = n1
n2 = Node(42)
n1.next = n2
n3 = Node(43)
n2.next = n3
n4 = Node(10)
n3.next = n4
z.traversal()
z.insert_at_beg(40)
z.insert_at_End(30)
z.traversal()