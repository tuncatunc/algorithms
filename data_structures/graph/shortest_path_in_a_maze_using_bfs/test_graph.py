import unittest
from graph import Graph


class GraphTestCase(unittest.TestCase):
  # Test for shortest paths
    def testVertices(self):
        g = Graph()
        g.add_vertex('A')
        g.add_vertex('B')
        g.add_vertex('C')

        vertices = g.vertices()
        expectedVertices = ['A', 'B', 'C']
        self.assertEqual(vertices, expectedVertices)

    def testEdges(self):
        g = Graph()
        g.add_vertex('A')
        g.add_vertex('B')
        g.add_vertex('C')
        g.add_edge(('A', 'B'))
        g.add_edge(('B', 'C'))
        g.add_edge(('C', 'A'))
        edges = g.edges()
        expected = [{'B', 'A'}, {'C', 'B'}, {'C', 'A'}]

        self.assertEqual(edges, expected)

    def testBfs(self):
        g = Graph()
        g.add_vertex('A')
        g.add_vertex('B')
        g.add_vertex('C')
        g.add_edge(('A', 'B'))
        g.add_edge(('B', 'C'))
        g.add_edge(('C', 'A'))
        queue = g.bfs('A')
        print(queue)

    def testMST_unweighted_graph(self):
        g = {"a": ["d", "f"],
             "b": ["c"],
             "c": ["b", "c", "d", "e"],
             "d": ["a", "c"],
             "e": ["c"],
             "f": ["d"]
             }
        graph = Graph(g)
        mst = graph.MST_unweighted_graph("a")
        self.assertEqual(mst, {'a': None, 'd': 'a', 'f': 'a', 'c': 'd', 'b': 'c', 'e': 'c'})

    def testDFS(self):
        g = {"a": ["d", "f"],
             "b": ["c"],
             "c": ["b", "c", "d", "e"],
             "d": ["a", "c"],
             "e": ["c"],
             "f": ["d"]
             }
        graph = Graph(g)
        graph.DFS("a")


if __name__ == '__main__':
    unittest.main()
