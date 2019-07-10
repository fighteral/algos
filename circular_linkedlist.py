class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:

    def __init__(self):
        self.head=None



    def remove_circular(self):
        slow=self.head
        fast=self.head

        while (fast != None):
            slow=slow.next
            fast=fast.next.next
            if slow == fast:
                break

        if fast is None:
            print "No circular dependency"

        else:
            slow=self.head
            while (slow.next != fast.next):
                slow=slow.next
                fast=fast.next

            fast.next = None

    def traverse(self):
        temp = self.head
        while temp:
            print temp.data
            temp=temp.next



ll=LinkedList()
ll.head=Node(1)
second=Node(2)
third=Node(3)
fourth=Node(4)

ll.head.next=second
second.next=third
third.next=fourth
fourth.next=second

ll.remove_circular()
ll.traverse()

