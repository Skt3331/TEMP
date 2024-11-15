from collections import deque

def bfs(graph, start_node):
    visited = set()       
    queue = deque([start_node])  
    
    while queue:
        
        current_node = queue.popleft()

        if current_node not in visited:
            print(current_node, end=" ")  
            visited.add(current_node)     
            
            
            
            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    queue.append(neighbor)


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("Breadth-First Search starting from node 'A':")
bfs(graph, 'A')