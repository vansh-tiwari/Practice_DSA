class AdjNode:
    def __init__(self, data):
        self.vertex = data
        self.next = None


class UnGraph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None]*self.V

    def addEdge(self, src, dest):

        node = AdjNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node

        node = AdjNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

    def showUnGraph(self):
        for x in range(self.V):
            print(x, end= " -- ")
            temp = self.graph[x]
            while temp:
                print(temp.vertex, end= " - ")
                temp = temp.next
            print("/")