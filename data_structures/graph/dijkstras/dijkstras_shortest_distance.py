import math
import sys

# https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/
class DijkstrasShortestDistance:
    def __init__(self, vertices, graph):
        self.V = vertices
        self.graph = graph
        self.parent = list(vertices)

    def pick_u(self, spSet, distances):
        # Pick a vertex not in spSet with min distance value
        V_diff_spSet = self.V - spSet
        distances_V_diff_spSet = list((i, distances[i]) for i in V_diff_spSet)
        u_tuple = min(distances_V_diff_spSet, key=lambda x: x[1])
        # include u in spSet
        u = u_tuple[0]
        spSet.add(u)
        return u

    def update_distance_values(self, u, distances, target = None):
        for v, distance in enumerate(self.graph[u]):
            if distance:
                # if sum of distance value of u (from source) and weight of edge u-v,
                # is less than the distance value of v,
                # then update the distance value of v.
                sum = distances[u] + self.graph[u][v]
                isLess = sum < distances[v]
                if isLess:
                    distances[v] = sum
                    self.parent[v] = u

    def print_solution(self, source, distances):
        print('Shortest distances from source', source)
        for idx, distance in enumerate(distances):
            print('vertex:',idx, '\tdistance:', distance, '\tparent:', self.parent[idx])

    # Shortest path from given vertex to all vertices or target vertex
    def dijkstra_shortest_distance(self, source, target = None):
        # Shortest path tree set
        sptSet = set()
        # Assign a distance value to all vertices, initialize to INFINITE
        distances = [sys.maxsize] * len(self.V)
        # Assign 0 to source vertex
        distances[source] = 0

        # While sptSet doesn't include all vertices in the graph
        while self.V - sptSet:
            u = self.pick_u(sptSet, distances)
            # update distance values from u
            self.update_distance_values(u, distances)
            if target and target in sptSet:
                break

        # print solution
        self.print_solution(source, distances)
        return {'distances': distances, 'parents': self.parent}

