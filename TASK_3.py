import heapq

def dijkstra(graph, start):
    # Initialize distances with infinity
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    
    # Min-heap to store the vertices to explore
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        # Nodes can get added to the priority queue multiple times. We only process a vertex the first time we remove it from the priority queue.
        if current_distance > distances[current_vertex]:
            continue
        
        # Explore the neighbors
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            
            # Only consider this new path if it's better
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# Example graph represented as an adjacency list
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Run Dijkstra's algorithm
start_vertex = 'A'
shortest_paths = dijkstra(graph, start_vertex)

# Print the shortest path distances from the start vertex
print(f"Shortest paths from {start_vertex}: {shortest_paths}")
