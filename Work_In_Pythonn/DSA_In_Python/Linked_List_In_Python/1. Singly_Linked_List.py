'''
singly linked-list := 
1. A linked list is a list of connected nodes, where each node points to (references) the node in front 
2. Traversal Is Possible In One Direction Only Which Is Forward Direction. (1-->2-->3-->Null)

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
'''class Node2:
    def __init__(self,data):
        self.data = data
        self.next = None 
'''
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
        newnode= Node(data) # creating an new node 
        newnode.next = self.head # making an connection between new-node and head-node
        self.head=newnode # changing head to new-node

# Insertion Of New Element at End.
    def insert_at_End(self,data):
        print()
        End = Node(data) # created an node.
        Temp2 = self.head # making the head variablle fixed.
        while Temp2.next is  not None: # running an while loop.
            Temp2=Temp2.next # pointing
        Temp2.next=End # connection between last node and  new node.

# Insertion Of New Element In Between.
    def insert_in_between(self,position,data):
        print()
        M1 =  Node(data) # creating node
        Fix = self.head #Fixing Head
        for i in range(1,position): 
            Fix = Fix.next #traversing  
        M1.next = Fix.next #connecting Node  where we want to insert the elements
        Fix.next=M1 # connecting New Node (M1) to first node.

# Deletion at beginning 
    def deletion_at_beg(self): 
        print()
        u6 = self.head #selecting the  head
        self.head = u6.next #shifting the head to next node
        u6.next=None # now the old node is  equal to none which means its disconnected.  
#  deletion_at_end
    def deletion_at_end(self):
        print()
        prev = self.head
        a = self.head.next
        while a.next is not None:
            a=a.next
            prev = prev.next
        prev.next = None
#  deletion_in_between
    def delete_in_between(self,position):
        print()
        prev = self.head # naming head
        a = self.head.next # 
        for i in range(1,position-1):
            a=a.next 
            prev = prev.next
        prev.next = a.next #disconnecton of the node with it's next node
        a.next = None


z=LinkedList1()
n1 = Node(1)
z.head = n1
n2 = Node(2)
n1.next = n2
n3 = Node(3)
n2.next = n3
n4 = Node(4)
n3.next = n4
z.insert_at_beg(9) #Output := 0-->1-->2-->3-->4-->
z.traversal() 
z.insert_at_End(5)  #Output := 0-->1-->2-->3-->4-->5-->
z.traversal()
z.insert_in_between(3,8)  #output := 0-->1-->2-->8-->3-->4-->5-->
z.traversal()
z.deletion_at_beg() #output := 1-->2-->8-->3-->4-->5--> 
z.traversal()
z.deletion_at_end() #output := 1-->2-->8-->3-->4-->
z.traversal()
z.delete_in_between(3) #Output := 1-->2-->3-->4-->
z.traversal()