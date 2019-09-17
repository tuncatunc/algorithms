class Graph:
  def __init__(self, graph):
    # Graph is adjacency graph
    self.graph = graph

  def print_path(self, start, target, parent):
    path = [start]
    current = start
    while current != target:
      current = parent[current]
      path.append(current)
    path.reverse()
    print(' <- '.join(str(x) for x in path))

  def print_path_to_all_vertices(self, start):
    visited = [start]
    queue = [start]
    parent = {}

    # Build parent map
    while queue:
      q = queue.pop(0)
      print("BFS =>", q)
      neighs = self.graph[q]
      for neigh in neighs:
        if neigh not in visited:
          queue.append(neigh)
          visited.append(neigh)
          parent[neigh] = q
    print(parent)

    # Print paths to start from each vertex
    for vertex in self.graph:
      self.print_path(vertex, start, parent)

graph = {
  0: [1, 2],
  1: [3],
  2: [0, 6, 5],
  3: [1, 4],
  4: [2, 3],
  5: [4, 6],
  6: [5]
}

graph = Graph(graph)
graph.print_path_to_all_vertices(2)