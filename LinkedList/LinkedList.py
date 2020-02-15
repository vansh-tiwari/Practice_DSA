class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    #Helps in adding new values
    def append(self, value):
        newNode = Node(value)
        #if self.head==None:
        #    self.head = newNode
        #    return self.head
        newNode.next = self.head
        self.head = newNode

    #Helps in adding value after specific index
    def appendAfter(self, index, value):
        newNode = Node(value)
        temp = self.head
        while index>1:
            temp = temp.next
            index-=1
        newNode.next = temp.next
        temp.next = newNode

    def reverse(self):
        prev = None
        cur = self.head
        while cur != None:
            nextNode = cur.next
            cur.next = prev
            prev = cur
            cur = nextNode
        self.head = prev

    #Helps in printing values of List
    def println(self):
        temp = self.head
        while temp:
            print(temp.value, end=" ")
            temp = temp.next
        print()
