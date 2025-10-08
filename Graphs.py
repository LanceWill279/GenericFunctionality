from collections import deque

def shortest_path(graph, start, goal):
    queue = deque([(start, [start])])
    visited = set()
    
    while queue:
        node, path = queue.popleft()
        if node == goal:
            return path
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"]
}

print(shortest_path(graph, "D", "F"))
# Output: ['A', 'C', 'F']
