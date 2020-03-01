from BinaryTree import BinaryTree
bt = BinaryTree()
vals = [9,5,7,2,6,10, 16, 1,3,8,17]
root = None
for x in vals:
    root = bt.insert(root, x)

# print("PreOrder")
# bt.preOrder(root)
# print()
print("InOrder")
bt.inOrder(root)
print()
# print("PostOrder")
# bt.postOrder(root)
# print()
# bt.search(root, 31)
root = bt.delete(root,5)
bt.inOrder(root)

