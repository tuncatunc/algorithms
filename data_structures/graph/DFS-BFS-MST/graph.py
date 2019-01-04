class Graph(object):
    def __init__(self, graph_dict=None):
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    def vertices(self):
        return list(self.__graph_dict.keys())

    def edges(self):
        return list(self.__generate_edges())

    def __generate_edges(self):
        edges = []
        for vertex in self.__graph_dict:
            for neigbor in self.__graph_dict[vertex]:
                if {vertex, neigbor} not in edges:
                    edges.append({vertex, neigbor})
        return edges

    def add_vertex(self, vertex):
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    # Edge is a tuple (vertex_1, vertex_2)
    def add_edge(self, edge):
        # edge is list, tuple, or set
        edge = set(edge)
        (vertext1, vertext2) = tuple(edge)
        if vertext1 in self.__graph_dict:
            self.__graph_dict[vertext1].append(vertext2)
        else:
            self.__graph_dict[vertext1] = [vertext2]

    def bfs(self, start):
        visited = []
        queue = []

        queue.append(start)
        visited.append(start)

        while queue:
            vertex = queue.pop(0)
            print('BFS=>', vertex)
            for neighbor in self.__graph_dict[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
        return queue

    # Minimum spanning tree in a unweighted graphs
    # DFS gives MST in a unweighted graph
    # that is
    # MST is a path travelling all nodes with minimum cost
    def MST_unweighted_graph(self, v0):
    # Let S = {v0} be a set of nodes initially containing v0
    # Mark v0
    # Parent[v0] = -1
    # While S is not empty
    #   Remove a vertex v from S
    #   For all edges (v,u)
    #     If u is unmarked
    #       Mark it and add it to S
    #       Parent[u] = v
      S = set(v0)
      visited = [v0]
      parent = {}
      parent[v0] = None

      while S:
        v = S.pop()
        for edge in self.__graph_dict[v]:
          if edge not in visited:
            visited.append(edge)
            S.add(edge)
            parent[edge] = v
      return parent

    def __DFS_Util(self, v, visited):
        visited.append(v)
        print("DFS =>", v)

        # Recur for all adjacent vertices
        for i in self.__graph_dict[v]:
            if i not in visited:
                self.__DFS_Util(i, visited)

    def DFS(self, v):
        visited = []
        self.__DFS_Util(v, visited)

    def __Is_Cyclic_Util(self, visited, v):
        visited.append(v)
        print('Visiting', v)

        for u in self.__graph_dict[v]:
            if u in visited and v not in self.__graph_dict[u]:
                return True
            else:
                return self.__Is_Cyclic_Util(visited, u)

        return False
    # Detect cycle in undirected graph
    # Using DFS
    # For every visited vertex ‘v’, 
    # if there is an adjacent ‘u’ such that u is already visited and u is not parent of v, 
    # then there is a cycle in graph.
    def Is_Cyclic(self):
        visited = []
        keys = list(self.__graph_dict.keys())
        v = keys[0]
        return self.__Is_Cyclic_Util(visited, v)

