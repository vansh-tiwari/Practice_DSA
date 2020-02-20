class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        if self.head==None:return True
        else:return False

    def push(self,data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def pop(self):
        if self.isEmpty():return
        # temp = self.head
        popped = self.head.value
        self.head = self.head.next
        return popped

    def println(self):
        temp = self.head
        while temp!=None:
            print(temp.value, end=" ")
            temp = temp.next
        print()
        