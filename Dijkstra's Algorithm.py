import heapq


def dijkstra(graph, start):
    # Step 1: Initialize distances and paths
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0  # Distance to source is 0
    previous_vertices = {vertex: None for vertex in graph}

    # Priority queue to pick the vertex with the smallest tentative distance
    priority_queue = [(0, start)]  # (distance, vertex)

    # keep track of visited vertices
    visited = set()

    history = []  # To store history of relaxation process

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # If the vertex is already visited skip it
        if current_vertex in visited:
            continue

        # Mark the current vertex as visited
        visited.add(current_vertex)

        # history message for each visited vertex
        history.append(f"Node({current_vertex}) with Weight:{current_distance} is added to the 'Visited' {visited}")

        # Explore neighbors
        for neighbor, weight in graph[current_vertex]:
            if neighbor in visited:
                continue

            new_distance = current_distance + weight
            if new_distance < distances[neighbor]:
                # Relax the edge
                distances[neighbor] = new_distance
                previous_vertices[neighbor] = current_vertex
                heapq.heappush(priority_queue, (new_distance, neighbor))

                # history message for relaxation
                history.append(
                    f"Relaxed: vertex[{neighbor}]: OLD: {distances[neighbor]}, NEW: {new_distance}, Paths: {previous_vertices}")
            else:
                history.append(f"No edge relaxation is needed for node, {neighbor}")

        # Handle case where there are no outgoing edges
        if not priority_queue and current_vertex == 'D':
            history.append(f"No unvisited outgoing edges from the node, {current_vertex}")

    # Final distances and paths
    history.append(f"Final Distances: {distances}")
    history.append(f"Final Paths: {previous_vertices}")

    return distances, previous_vertices, history


graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('C', 3), ('D', 2), ('E', 3)],
    'C': [('B', 1), ('D', 4), ('E', 5)],
    'D': [],  # D has no outgoing edges
    'E': [('D', 1)]  # E points to D with a weight of 1
}

# Run Dijkstra's algorithm from vertex 'A'
start_vertex = 'A'
distances, previous_vertices, history = dijkstra(graph, start_vertex)

# Print the history of the relaxation process
for entry in history:
    print(entry)


print("\nFinal Distances:", distances)
print("Final Paths:", previous_vertices)


