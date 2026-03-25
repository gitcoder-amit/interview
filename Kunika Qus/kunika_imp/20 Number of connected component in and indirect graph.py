'''Not available in Leetcode, but here’s a Python implementation to find the number of connected components in an undirected graph using Depth First Search (DFS):'''



def count_connected_components(graph):
    visited = [False for _ in range(len(graph))]
    count = 0

    def dfs(node):
        visited[node] = True
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    for vertex in graph:
        if vertex not in visited:
            count += 1
            dfs(vertex)

    return count