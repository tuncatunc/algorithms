class GraphAdj:
  def __init__(self, V):
    self.V = V
    self.adj = [[0 for x in range(V)] for y in range(V)]

  def addEdge(self, u, v):
    self.adj[u][v] = 1
    self.adj[v][u] = 1

  def removeEdge(self, u, v):
    self.adj[u][v] = 0
    self.adj[v][u] = 0

  def isValid(self, u, v):
    return self.adj[u][v] == 1
