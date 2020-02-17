from LinkedList import *
ll = LinkedList()

#No. to input in list
n = int(input())

#Inserting in order
for x in range(n,0,-1):
    ll.insertFirst(x)

# ll.insertAfter(4, 1229)
# ll.println()
# ll.insertLast(25000)
# ll.println()
# ll.reverse()
# ll.println()
# ll.deleteFirst()
ll.println()
ll.length()
