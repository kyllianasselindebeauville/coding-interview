# 4.1 Route Between Nodes

import unittest
from graph import Graph


def route_between_nodes(graph, source, destination):
    if source not in graph.nodes or destination not in graph.nodes:
        return False

    queue, visited = [graph.nodes[source]], set()

    while len(queue) > 0:
        current = queue.pop()
        visited.add(current)

        if current is graph.nodes[destination]:
            return True

        for neighbor in current.neighbors:
            if neighbor not in visited:
                queue.append(neighbor)

    return False


class Test(unittest.TestCase):
    def test_route_between_nodes(self):
        graph = Graph({
            0: [1, 4, 5],
            1: [3, 4],
            2: [1],
            3: [2, 4],
            4: [],
            5: [],
        })
        self.assertTrue(route_between_nodes(graph, 2, 4))
        self.assertFalse(route_between_nodes(graph, 2, 5))

        graph = Graph({
            'f': ['g', 'i'],
            'g': ['h'],
            'h': [],
            'i': ['g', 'k'],
            'j': ['i'],
            'k': []
        })
        self.assertTrue(route_between_nodes(graph, 'f', 'k'))
        self.assertFalse(route_between_nodes(graph, 'f', 'j'))


if __name__ == '__main__':
    unittest.main()
