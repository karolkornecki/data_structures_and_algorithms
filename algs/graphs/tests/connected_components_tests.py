import unittest

from graphs.connected_components import connected_components
from graphs.undirected_graph import UndirectedGraph


class ConnectedComponentsTestCase(unittest.TestCase):

    def test_connected_components(self):
        # given
        g = UndirectedGraph()
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(0, 5)
        g.add_edge(0, 6)
        g.add_edge(5, 3)
        g.add_edge(5, 4)
        g.add_edge(6, 4)
        g.add_edge(4, 3)

        g.add_edge(7, 8)

        g.add_edge(9, 10)
        g.add_edge(9, 11)
        g.add_edge(9, 12)
        g.add_edge(11, 12)

        # when
        number_of_cc, identifiers = connected_components(g)

        # then
        self.assertEqual(3, number_of_cc)
        self.assertEqual([0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 2, 2, 2], identifiers)


if __name__ == '__main__':
    unittest.main()