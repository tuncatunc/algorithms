from GraphAdj import GraphAdj
from  DisjointSet import DisjointSet

class FindBridges:
  def __init__(self, V):
    self.graph = GraphAdj(V)
    self.disjointSet = DisjointSet(V)
    self.V = V

  def addEdge(self, u, v):
    self.graph.addEdge(u, v)

  def isConnected(self):
    # For each edge in the graph
    # Create a set for each vertex of the edge
    # Return False, if another disjoint set is found
    for v in range(self.V):
      self.disjointSet.makeSet(v)

    for u in range(self.V):
      for v in range(self.V):
        if self.graph.isValid(u, v):
          uf = self.disjointSet.findSet(u)
          vf = self.disjointSet.findSet(v)

          self.disjointSet.unionSets(uf, vf)

    # Is there more than 1 set in the disjoint set
    first = self.disjointSet.findSet(0)
    for v in range(self.V):
      vf = self.disjointSet.findSet(v)
      if vf != first:
        return False

    return True



  # Find critical edge
  # For each edge
  #   Remove edge from graph
  #   Check if the rest of the vertices still create a single disjoint set
  def solve(self):
    criticalEdges = []
    for u in range(self.V):
      for v in range(self.V):
        if self.graph.isValid(u, v):
          self.graph.removeEdge(u, v)

          if not self.isConnected():
            criticalEdges.append((u, v))

          self.graph.addEdge(u, v)

    return criticalEdges


if __name__ == "__main__":
    V = 5
    problem = FindBridges(V)
    problem.addEdge(0, 1)
    problem.addEdge(0, 2)
    problem.addEdge(0, 3)
    problem.addEdge(1, 2)
    problem.addEdge(3, 4)

    bridges = problem.solve()
    print(f'Bridges in the graph {bridges}')

