
from collections import deque

def bidirectional_search(graph, start, goal):

    if start == goal:
        return [start]

    forward_queue = deque([start])
    backward_queue = deque([goal])

    forward_visited = {start: None}
    backward_visited = {goal: None}

    while forward_queue and backward_queue:

        # Forward search
        current = forward_queue.popleft()

        for neighbor in graph[current]:
            if neighbor not in forward_visited:
                forward_visited[neighbor] = current
                forward_queue.append(neighbor)

                if neighbor in backward_visited:
                    return build_path(
                        neighbor,
                        forward_visited,
                        backward_visited
                    )

        # Backward search
        current = backward_queue.popleft()

        for neighbor in graph[current]:
            if neighbor not in backward_visited:
                backward_visited[neighbor] = current
                backward_queue.append(neighbor)

                if neighbor in forward_visited:
                    return build_path(
                        neighbor,
                        forward_visited,
                        backward_visited
                    )

    return None


def build_path(meeting, forward, backward):

    path = []

    # Source to meeting point
    node = meeting
    while node is not None:
        path.append(node)
        node = forward[node]

    path.reverse()

    # Meeting point to goal
    node = backward[meeting]
    while node is not None:
        path.append(node)
        node = backward[node]

    return path


# Define the graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E', 'G'],
    'G': ['F']
}

source = 'A'
goal = 'G'

path = bidirectional_search(graph, source, goal)

if path:
    print("Path found:", " -> ".join(path))
    print("Path length:", len(path) - 1)
else:
    print("No path found")
