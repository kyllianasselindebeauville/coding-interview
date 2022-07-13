# 4.1 Route Between Nodes

from graph import Graph


def route_between_nodes(graph, source, destination):
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


def main():
    graph = Graph({
        'f': ['g', 'i'],
        'g': ['h'],
        'h': [],
        'i': ['g', 'k'],
        'j': ['i'],
        'k': []
    })

    print(route_between_nodes(graph, 'f', 'k'))


if __name__ == '__main__':
    main()
