from LinkedList import *
ll = LinkedList()
n = int(input())
for _ in range(n):
    ll.append(int(input()))

ll.appendAfter(3, 101)
ll.println()
