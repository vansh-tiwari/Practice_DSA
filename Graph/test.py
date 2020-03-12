from Graph import UnGraph
vertices = 5
ug = UnGraph(vertices)
ug.addEdge(0, 1)
ug.addEdge(0, 4)
ug.addEdge(1, 2)
ug.addEdge(1, 3)
ug.addEdge(1, 4)
ug.addEdge(2, 3)
ug.addEdge(3, 4)
ug.showUnGraph()
