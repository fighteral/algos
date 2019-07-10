class linkedlist:
    def __init__(self):
        self.head=None

    def traverse(self):
        temp = self.head
        while temp:
            print temp.data
            temp=temp.next


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


llist=linkedlist()

llist.head=Node(1)

one=Node(2)
second=Node(3)

llist.head.next=second

second.next=one

llist.traverse()