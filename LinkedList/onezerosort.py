from DoublyLinkedList import DoublyLinkedList

dll = DoublyLinkedList()
nums = [1,1,0,0,1,0,1,0,0,1]
for x in nums:
    dll.insertFirst(x)

dll.println()
dll.onezero()
dll.println()