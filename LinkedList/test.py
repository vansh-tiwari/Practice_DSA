from LinkedList import LinkedList
from DoublyLinkedList import DoublyLinkedList

ll = LinkedList()
dll = DoublyLinkedList()

#No. to input in list
n = int(input())

#Inserting in order
for x in range(n):
    dll.insertFirst(x)

# ll.insertAfter(4, 1229)
# ll.insertLast(25000)
# ll.reverse()
# ll.deleteFirst()
# ll.println()
# ll.length()
dll.println()
dll.rev_println()