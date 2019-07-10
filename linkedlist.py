class Linkedlist:
    def __init__(self):
        self.head=None

    def push(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    def insert(self,previous,data):
        new_node=Node(data)
        new_node.next=previous.next
        previous.next=new_node

    def insert_end(self,data):
        new_node = Node(data)

        temp=self.head
        while temp.next:
            temp=temp.next


        temp.next=new_node

    def delete(self,value):
        temp = self.head
        prev=None
        while temp is not None:
            if temp.data == value:
                break
            prev=temp
            temp=temp.next

        if (temp==None):
            return

        prev.next=temp.next
        


    def traverse(self):
        temp = self.head
        while temp:
            print temp.data
            temp=temp.next



class Node:
    def __init__(self,data):
        self.data = data
        self.next = None




ll=Linkedlist()

ll.head=Node(1)
second=Node(2)
third=Node(3)

ll.head.next=second
second.next=third

ll.push(6)
ll.insert(ll.head.next,9)
ll.insert_end(4)
ll.delete(2)
ll.traverse()




