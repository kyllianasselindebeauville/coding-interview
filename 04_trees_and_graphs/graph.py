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

            for current, neighbors in adjacency_list.items():
                for n in neighbors:
                    if (n in self.nodes and
                        self.nodes[n] not in self.nodes[current].neighbors):
                        self.nodes[current].neighbors.append(self.nodes[n])

    def __str__(self):
        return '\n'.join([
            f'{str(node)}: {", ".join([str(n) for n in node.neighbors])}'
            for node in self.nodes.values()
        ])
