class LinkeList:
    def __init__(self):
        self.head=None

    def push(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    def remove_duplicate(self):
        d={}
        temp=self.head
        prev=None
        while temp:

            if temp.data in d.keys():
                break;

            d[temp.data]=1
            prev = temp
            temp=temp.next

        prev.next=temp.next

    def traverse(self):
        temp = self.head
        while temp:
            print temp.data
            temp=temp.next




class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

ll=LinkeList()

ll.head=Node(1)
second=Node(2)
third=Node(3)

ll.head.next=second
second.next=third

ll.push(2)
ll.remove_duplicate()
ll.traverse()


