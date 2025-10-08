from collections import deque
import heapq

# --- Hardcoded graph (Directed + Weighted) ---
graph = {
    "A": {"B": 4, "C": 2},
    "B": {"C": 5, "D": 10},
    "C": {"E": 3},
    "D": {"F": 11},
    "E": {"D": 4},
    "F": {}
}

# --- Traversal algorithms ---

def bfs_path(graph, start, goal):
    """Unweighted shortest path using BFS."""
    queue = deque([(start, [start])])
    visited = set([start])
    
    while queue:
        node, path = queue.popleft()
        if node == goal:
            return path
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return None


def dfs_path(graph, start, goal, path=None, visited=None):
    """Find any path using DFS (not necessarily shortest)."""
    if visited is None:
        visited = set()
    if path is None:
        path = [start]
    
    visited.add(start)
    if start == goal:
        return path
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            result = dfs_path(graph, neighbor, goal, path + [neighbor], visited)
            if result:
                return result
    return None


def dijkstra_path(graph, start, goal):
    """Weighted shortest path using Dijkstra's algorithm."""
    pq = [(0, start, [start])]  # (cost, node, path)
    visited = set()
    
    while pq:
        cost, node, path = heapq.heappop(pq)
        if node in visited:
            continue
        visited.add(node)
        
        if node == goal:
            return path, cost
        
        for neighbor, weight in graph[node].items():
            if neighbor not in visited:
                heapq.heappush(pq, (cost + weight, neighbor, path + [neighbor]))
    return None, float('inf')


# --- User Interface ---
def main():
    print("Graph Path Finder")
    print("-----------------")
    print("Available nodes:", ", ".join(graph.keys()))
    print("Algorithms: BFS, DFS, Dijkstra")
    
    start = input("Enter start node: ").upper().strip()
    goal = input("Enter goal node: ").upper().strip()
    algo = input("Select algorithm (BFS/DFS/Dijkstra): ").lower().strip()
    
    if start not in graph or goal not in graph:
        print("❌ Invalid nodes.")
        return
    
    if algo == "bfs":
        path = bfs_path(graph, start, goal)
        print("→ BFS Path:", path if path else "No path found.")
    elif algo == "dfs":
        path = dfs_path(graph, start, goal)
        print("→ DFS Path:", path if path else "No path found.")
    elif algo == "dijkstra":
        path, cost = dijkstra_path(graph, start, goal)
        if path:
            print(f"→ Dijkstra Path: {path} (Cost: {cost})")
        else:
            print("No path found.")
    else:
        print("❌ Unknown algorithm. Please choose BFS, DFS, or Dijkstra.")


if __name__ == "__main__":
    main()
