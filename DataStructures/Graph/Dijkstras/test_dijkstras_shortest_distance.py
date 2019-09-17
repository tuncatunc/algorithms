import unittest
from dijkstras_shortest_distance import DijkstrasShortestDistance

class DijkstraShortestDistanceTestCase(unittest.TestCase):
  # Test for shortest paths
    def testShortestDistance(self):
        V = set(range(9))
        graph = [[0,  4,  0,  0,  0,  0,  0,  8,  0],
                [4,  0,  8,  0,  0,  0,  0,  11, 0],
                [0,  8,  0,  7,  0,  4,  0,  0,  2],
                [0,  0,  7,  0,  9,  14, 0,  0,  0],
                [0,  0,  0,  9,  0,  10, 0,  0,  0],
                [0,  0,  4,  14, 10, 0,  2,  0,  0],
                [0,  0,  0,  0,  0,  2,  0,  1,  6],
                [8,  11, 0,  0,  0,  0,  1,  0,  7],
                [0,  0,  2,  0,  0,  0,  6,  7,  0]
                ]

        g = DijkstrasShortestDistance(V, graph)

        shortestDistances = g.dijkstra_shortest_distance(0)

        expectedDistances = [0, 4, 12, 19, 21, 11, 9, 8, 14]
        self.assertEqual(shortestDistances, expectedDistances)

        

if __name__ == '__main__':
    unittest.main()