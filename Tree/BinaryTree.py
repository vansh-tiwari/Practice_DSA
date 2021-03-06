class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, tempNode, val):
        newNode = Node(val)
        #RECURSIVE APPROACH
        if tempNode is None: return newNode
        if val < tempNode.data: tempNode.left = self.insert(tempNode.left, val)
        else: tempNode.right = self.insert(tempNode.right, val)
        return tempNode

        #ITERATIVE APPROACH
        # print("newNode with value {} is created".format(newNode.data))
        # if self.root == None:
        #     self.root = newNode
        #     # print("Root is None and pointed to newNode with value {} is created".format(newNode.data))
        #     return self.root
        # else:
        #     cur = self.root
        #     while(True):
        #         if data < cur.data:
        #             #Left
        #             # print("Left {}".format(cur.data))
        #             if(cur.left is None):
        #                 cur.left = newNode
        #                 return self.root
        #             cur = cur.left
        #         else:
        #             #Right
        #             # print("Right {}".format(cur.data))
        #             if(cur.right is None):
        #                 cur.right = newNode
        #                 return self.root
        #             cur = cur.right

    def search(self, tempNode, val):
        if tempNode is None:
            print("False")
            return
        temp = tempNode
        if val < temp.data: self.search(temp.left, val)
        elif val > temp.data: self.search(temp.right, val)
        elif val==temp.data:
            print("True")
            return
        else: return
    
    def preOrder(self, tempNode):
        temp = tempNode
        if temp is None:
            return
        print("[{}]".format(temp.data))
        if temp.left is not None:
            print("Left {}  ".format(temp.data), end="-> ")
            self.preOrder(temp.left)
        if temp.right is not None:
            print("Right {}  ".format(temp.data), end="-> ")
            self.preOrder(temp.right)


    def inOrder(self, tempNode):
        temp = tempNode
        if temp is None:return
        if temp.left is not None:
            print("Left {}  ".format(temp.data), end="-> ")
            self.inOrder(temp.left)
        print("[{}]".format(temp.data))
        if temp.right is not None:
            print("Right {}  ".format(temp.data), end="-> ")
            self.inOrder(temp.right)


    def postOrder(self, tempNode):
        temp = tempNode
        if temp is None:return
        if temp.left is not None:
            print("Left {}  ".format(temp.data), end="-> ")
            self.postOrder(temp.left)
        if temp.right is not None:
            print("Right {}  ".format(temp.data), end="-> ")
            self.postOrder(temp.right)
        print("[{}]".format(temp.data))

    def delete(self, nodeToDelete, val):
        head = nodeToDelete
        if head is None: return
        if val < head.data: head.left=self.delete(head.left, val)
        elif val > head.data: head.right=self.delete(head.right, val)
        else:
            if head.left is None:
                temp = head.right
                head = None
                return temp
            elif head.right is None:
                temp = head.left
                head = None
                return temp
            
            temp = head.right
            while temp.left is not None:
                temp = temp.left
            
            head.data = temp.data
            head.right = self.delete(head.right, temp.data)
        return head