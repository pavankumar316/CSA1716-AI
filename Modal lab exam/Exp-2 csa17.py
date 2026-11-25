
def beam_search(graph, heuristic, start, goal, beam_width):

    beam = [[start]]

    while beam:

        candidates = []

        for path in beam:
            node = path[-1]

            if node == goal:
                return path

            for neighbor in graph.get(node, []):
                new_path = path + [neighbor]
                candidates.append(new_path)

        # Sort paths based on heuristic values
        candidates.sort(
            key=lambda path: heuristic[path[-1]]
        )

        # Select the best K paths
        beam = candidates[:beam_width]

    return None


# State-space graph
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['G', 'H'],
    'D': ['I'],
    'E': [],
    'F': [],
    'G': [],
    'H': [],
    'I': []
}

# Heuristic values
heuristic = {
    'A': 8,
    'B': 6,
    'C': 4,
    'D': 7,
    'E': 5,
    'F': 3,
    'G': 0,
    'H': 2,
    'I': 6
}

start = 'A'
goal = 'G'
beam_width = 2

path = beam_search(
    graph, heuristic, start, goal, beam_width
)

if path:
    print("Best Path:", " -> ".join(path))
    print("Path Cost:", len(path) - 1)
else:
    print("Goal not found")
