class Dnode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insertFirst(self, value):
        newNode = Dnode(value)
        newNode.next = self.head
        newNode.prev = None
        if self.head != None:
            self.head.prev = newNode
        self.head = newNode

    def println(self):
        if self.head == None:
            return
        temp = self.head
        while temp!=None:
            last = temp
            print(temp.value, end=" ")
            temp = temp.next
        print()
        while last!=None:
            print(last.value, end=" ")
            last = last.prev
        print()
        
