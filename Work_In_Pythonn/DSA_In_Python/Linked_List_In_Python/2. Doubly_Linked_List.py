'''
1. Doubly Linked List Is a List In Which we The Head Node Or The Selectedd Node Is Connected With It's Previous And Next Node.
2. Here Traveral Is  Possible In Both The Directions
Example := 1<-->2<-->3<-->4<-->Null.
'''
#Creating node 
'''class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
        # forward Traversal Code
        a= self.head
        while a is not None:
            print(a.data,end="-->")
            a = a.next

        #backward Traversal Code
        a = self.head
        while a.next is not None:
            a=a.next
        while a is not None:
            print(a.data,end="==>")
            a=a.prev
'''

class Node():
    def __init__(self,data):
        self.data = data
        self.next = None 
        self.prev = None
class doubly_Linked_List():
    def __init__(self):
        self.head = None
    def traversal_in_forward(self):
        if  self.head is None:
            print("doubly  linked list is empty")
        else:
            a=self.head
            while a is not None:
                print(a.data,end="   ")
                a=a.next
    
    def traversal_in_backward(self):
        print()
        if self.head is None:
            print("doubly linked list is empty")
        else:
            a = self.head
            while  a.next is  not None:
                a=a.next
            while a is not None:
                print(a.data,end="   ")
                a=a.prev

    def insert_at_beg(self,data):
        print()
        nn = Node(data) # creating newnode
        a = self.head
        a.prev=nn
        nn.next = a
        self.head  = nn

    def insert_at_end(self,data):
        print()
        any = Node(data)
        a = self.head
        while a.next is not None:
            a=a.next
        a.next = any
        any.prev = a
    def insertion_at_fixed_position(self,position,data):
        print()
        n = Node(data)
        a=self.head
        for i in range(0,position):
            a=a.next
        n.next = a.next
        n.prev = a.prev
        a.prev = n
        a.next = n
    def deletion_at_beg(self):
        print()
        n = self.head
        self.head=n.next
        n.next = None
        self.head.prev = None
    
    def delete_at_end(self):
        print()
        prev = self.head
        a = self.head.next
        while a.next is not None:
            a = a.next
            prev = prev.next
        a.next = None
        prev.next = None
    
    def delete_in_between(self,position):
        print()
        a = self.head.next
        prev = self.head
        for i in range(0,position - 1):
            a= a.next
            prev = prev.next
        prev.next = a.next
        a.next.prev = prev
        a.next = None
        a.prev = None

        
s=doubly_Linked_List()
n1 = Node(104)
s.head = n1
n2 = Node(110)
n1.next = n2
n2.prev=n1
n3 = Node(120)
n2.next =n3
n3.prev =n2
n4 = Node(103)
n3.next  = n4
n4.prev  = n3
s.traversal_in_forward()
s.traversal_in_backward()
s.insert_at_beg(34)
s.traversal_in_forward()
s.traversal_in_backward()
s.insert_at_end(456)
s.traversal_in_forward()
s.traversal_in_backward()
s.insertion_at_fixed_position(2,786)
s.traversal_in_forward()
s.traversal_in_backward()
s.deletion_at_beg()
s.traversal_in_forward()
s.traversal_in_backward()
s.delete_at_end()
s.traversal_in_forward()
s.traversal_in_backward()
s.delete_in_between(3)
s.traversal_in_forward()
s.traversal_in_backward()
