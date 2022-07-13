# Graph

class GraphNode:
    def __init__(self, data=None, neighbors=None):
        self.data = data
        self.neighbors = neighbors if neighbors is not None else []

    def __str__(self):
        return str(self.data)


class Graph:
    def __init__(self, adjacency_list=None):
        self.nodes = dict()

        if adjacency_list is not None:
            for node in adjacency_list:
                self.nodes[node] = GraphNode(node)

            for node, neighbors in adjacency_list.items():
                self.nodes[node].neighbors.extend([self.nodes[n] for n in neighbors])
