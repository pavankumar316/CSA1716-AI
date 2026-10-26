graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

heuristic = {
    'A': 6,
    'B': 4,
    'C': 2,
    'D': 5,
    'E': 3,
    'F': 1,
    'G': 0
}

def best_first_search(start, goal):
    open_list = [start]
    visited = []

    while open_list:
        open_list.sort(key=lambda node: heuristic[node])
        current = open_list.pop(0)

        if current in visited:
            continue

        print(current, end=" ")
        visited.append(current)

        if current == goal:
            print("\nGoal found!")
            return

        for neighbor in graph[current]:
            if neighbor not in visited and neighbor not in open_list:
                open_list.append(neighbor)

    print("\nGoal not found!")

start = 'A'
goal = 'G'

print("Best First Search Traversal:")
best_first_search(start, goal)
