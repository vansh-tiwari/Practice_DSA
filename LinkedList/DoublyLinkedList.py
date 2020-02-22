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
        if self.head == None:
            self.tail = newNode
        else:
            self.head.prev = newNode
        self.head = newNode

    #Incomplete
    # def onezero(self):
    #     zero = self.head
    #     one = self.tail
    #     while zero!=None or one!=None:
    #         if zero.value==0:zero=zero.next
    #         if one.value==1: one=one.prev
    #         if zero.value==1 and one.value==0:
    #             zero.value, one.value = one.value, zero.value

    def println(self):
        if self.head == None:
            return
        temp = self.head
        while temp!=None:
            # last = temp
            print(temp.value, end=" ")
            temp = temp.next
        print()
        
    def rev_println(self):
        # while last!=None:
        #     print(last.value, end=" ")
        #     last = last.prev
        # print()
        revtemp = self.tail
        while revtemp!=None:
            # revtemp.value+=10
            print(revtemp.value, end=" ")
            revtemp = revtemp.prev
        print()
        
