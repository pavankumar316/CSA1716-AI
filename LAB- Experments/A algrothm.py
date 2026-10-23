def astar(graph, heuristic, start, goal):
    open_list = [(heuristic[start], 0, start, [start])]
    visited = set()

    while open_list:
        open_list.sort()
        f, g, node, path = open_list.pop(0)

        if node == goal:
            print("Shortest Path:", path)
            print("Total Cost:", g)
            return

        if node in visited:
            continue

        visited.add(node)

        for neighbour, cost in graph[node]:
            if neighbour not in visited:
                new_g = g + cost
                new_f = new_g + heuristic[neighbour]
                open_list.append(
                    (new_f, new_g, neighbour, path + [neighbour])
                )

    print("No path found")


graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 5), ('E', 2)],
    'C': [('E', 1)],
    'D': [('G', 3)],
    'E': [('G', 5)],
    'G': []
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 3,
    'E': 4,
    'G': 0
}

astar(graph, heuristic, 'A', 'G')
