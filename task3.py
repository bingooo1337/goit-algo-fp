import heapq


def dijkstra(graph, start):
    queue = []
    heapq.heappush(queue, (0, start))

    distances = {node: float("inf") for node in graph}
    distances[start] = 0

    previous_nodes = {node: None for node in graph}

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    return distances, previous_nodes


def create_graph(edges):
    graph = {}
    for edge in edges:
        start, end, weight = edge
        if start not in graph:
            graph[start] = {}
        if end not in graph:
            graph[end] = {}
        graph[start][end] = weight
        graph[end][start] = weight
    return graph


def get_path(previous_nodes, start, end):
    path = []
    current_node = end
    while current_node is not None:
        path.insert(0, current_node)
        current_node = previous_nodes[current_node]
    if path[0] == start:
        return path
    else:
        return []


if __name__ == "__main__":
    edges = [
        ("A", "B", 1),
        ("A", "C", 1),
        ("B", "C", 2),
        ("B", "D", 1),
        ("C", "D", 1)
    ]

    graph = create_graph(edges)
    start_node = "A"
    distances, previous_nodes = dijkstra(graph, start_node)

    for node, distance in distances.items():
        print(f"From {start_node} to {node}: {distance}")

    for vertex in graph:
        if vertex != start_node:
            path = get_path(previous_nodes, start_node, vertex)
            print(f"Path from {start_node} to {vertex}: {' -> '.join(path)}")
