from Stack import Stack

stack = Stack()
n = int(input())
for x in range(n):
    stack.push(x)

stack.println()
print(stack.pop())
stack.println()
# print(stack.isEmpty())