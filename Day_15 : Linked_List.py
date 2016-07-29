class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Solution:
    def display(self,head):
        current = head
        while current:
            print current.data,
            current = current.next

    def insert(self,head,data):
        #Complete this method
        node = Node(data)
        if head==None:
            return node
        else:
            curr_node = head
            while curr_node.next!=None:
                curr_node = curr_node.next

            curr_node.next = node
        return head

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)
mylist.display(head);
