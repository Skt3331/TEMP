# Q.5 Implement AO star Algorithm

# Cost to find the AND and OR path
def calculate_cost(H, condition, weight=1):
    cost = {}
    
    if 'AND' in condition:
        AND_nodes = condition['AND']
        path_and = ' AND '.join(AND_nodes)
        cost[path_and] = sum(H[node] + weight for node in AND_nodes)

    if 'OR' in condition:
        OR_nodes = condition['OR']
        path_or = ' OR '.join(OR_nodes)
        cost[path_or] = min(H[node] + weight for node in OR_nodes)

    return cost

# Update the cost
def update_cost(H, conditions, weight=1):
    main_nodes = list(conditions.keys())
    main_nodes.reverse()  # Process in reverse order
    least_cost = {}

    for key in main_nodes:
        condition = conditions[key]
        current_cost = calculate_cost(H, condition, weight)
        print(f"{key}: {condition} >>> {current_cost}")
        
        H[key] = min(current_cost.values())
        least_cost[key] = current_cost

    return least_cost

# Print the shortest path
def shortest_path(start, updated_cost, H):
    path = start
    
    if start in updated_cost:
        min_cost = min(updated_cost[start].values())
        keys = list(updated_cost[start].keys())
        values = list(updated_cost[start].values())
        index = values.index(min_cost)

        # Find minimum path key
        next_nodes = keys[index].split()

        # Handle OR path
        if len(next_nodes) == 1:
            start = next_nodes[0]
            path += '<--' + shortest_path(start, updated_cost, H)
        # Handle AND path
        else:
            path += '<--(' + keys[index] + ') '
            start = next_nodes[0]
            path += '[' + shortest_path(start, updated_cost, H) + ' + '
            start = next_nodes[-1]
            path += shortest_path(start, updated_cost, H) + ']'

    return path

# Example data
H = {'A': -1, 'B': 5, 'C': 2, 'D': 4, 'E': 7, 'F': 9, 'G': 3, 'H': 0, 'I': 0, 'J': 0}

conditions = {
    'A': {'OR': ['B'], 'AND': ['C', 'D']},
    'B': {'OR': ['E', 'F']},
    'C': {'OR': ['G'], 'AND': ['H', 'I']},
    'D': {'OR': ['J']}
}

# Weight
weight = 1

# Updated cost
print('Updated Cost:')
updated_cost = update_cost(H, conditions, weight)
print('*' * 75)
print('Shortest Path:\n', shortest_path('A', updated_cost, H))

