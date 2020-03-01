class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        newNode = Node(data)
        # print("newNode with value {} is created".format(newNode.data))
        if self.root == None:
            self.root = newNode
            # print("Root is None, newNode with value {} is created".format(newNode.data))
            return self.root
        else:
            cur = self.root
            while(True):
                if data < cur.data:
                    #Left
                    # print("Left {}".format(cur.data))
                    if(cur.left is None):
                        cur.left = newNode
                        return self.root
                    cur = cur.left
                else:
                    #Right
                    # print("Right {}".format(cur.data))
                    if(cur.right is None):
                        cur.right = newNode
                        return self.root
                    cur = cur.right
    
    def preOrder(self, temp):
        if temp is None:
            return
        print("[{}]".format(temp.data))
        if temp.left is not None:
            print("Left {}  ".format(temp.data), end="-> ")
            self.preOrder(temp.left)
        if temp.right is not None:
            print("Right {}  ".format(temp.data), end="-> ")
            self.preOrder(temp.right)


    def inOrder(self, temp):
        if temp is None:return
        if temp.left is not None:
            print("Left {}  ".format(temp.data), end="-> ")
            self.inOrder(temp.left)
        print("[{}]".format(temp.data))
        if temp.right is not None:
            print("Right {}  ".format(temp.data), end="-> ")
            self.inOrder(temp.right)


    def postOrder(self, temp):
        if temp is None:return
        if temp.left is not None:
            print("Left {}  ".format(temp.data), end="-> ")
            self.postOrder(temp.left)
        if temp.right is not None:
            print("Right {}  ".format(temp.data), end="-> ")
            self.postOrder(temp.right)
        print("[{}]".format(temp.data))