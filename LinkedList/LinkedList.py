class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    #Helps in adding new values
    def insertFirst(self, value):
        newNode = Node(value)
        #if self.head==None:
        #    self.head = newNode
        #    return self.head
        newNode.next = self.head
        self.head = newNode

    #Helps in adding value after specific index
    def insertAfter(self, index, value):
        newNode = Node(value)
        temp = self.head
        if self.head == None:
            self.head = newNode
            return

        while index>1:
            temp = temp.next
            index-=1
        newNode.next = temp.next
        temp.next = newNode

    #Adding value at last of list
    def insertLast(self, value):
        newNode = Node(value)
        temp = self.head

        if self.head == None:
            self.head = newNode
            return

        while temp.next!=None:
            temp = temp.next
        temp.next = newNode

    #Reversing list
    def reverse(self):
        prev = None
        cur = self.head
        while cur != None:
            nextNode = cur.next
            cur.next = prev
            prev = cur
            cur = nextNode
        self.head = prev

    #Delete first element from list
    def deleteFirst(self):
        if self.head == None:
            return
        temp = self.head
        self.head = self.head.next
        temp.next = None

    def deleteValue(self,value):
        if self.head == None:
            return
        temp = self.head
        while temp.next.value != value:
            temp = temp.next
        prev = temp.next
        temp.next = temp.next.next
        prev.next=None

    #Helps in printing values of List
    def println(self):
        temp = self.head
        count = 0
        while temp:
            print(temp.value, end=" ")
            temp = temp.next
            count+=1
        print()
    
    def length(self):
        temp = self.head
        count = 0
        while temp:
            temp = temp.next
            count+=1
        print(count)