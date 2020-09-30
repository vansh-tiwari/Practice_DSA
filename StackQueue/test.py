from Stack import Stack

stack = Stack()
n = int(input())
for x in range(n):
    #adds an element to the stack
    stack.push(x)

stack.println()
#removes the most recently added element
print(stack.pop())
stack.println()
# print(stack.isEmpty())
