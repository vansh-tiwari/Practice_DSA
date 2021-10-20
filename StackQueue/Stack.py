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

# =======================        
# using collecions module
# =======================

class stack():
	def __init__(self):
		self.container = deque()
	
	def push(self, data):
		self.container.append(data)
	
	def pop(self):
		self.container.pop()

	def printStack(self):
		print(self.container)			

if __name__ == '__main__':
	from collections import deque
	qu = stack()
	qu.push('hello friend')
	qu.push('I hope you can see this')
	qu.push('fsociety.dat')
	qu.pop()
	qu.printStack()
