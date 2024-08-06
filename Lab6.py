graph = {
    'A': ['B','F','D','E'],
    'B': ['K', 'J'],
    'C': [],
    'D': ['G'],
    'E': ['C','H','I'],
    'F': [],
    'G': [],
    'H': [],
    'I': ['L'],
    'J': [],
    'K': ['N','M'],
    'L':[],
    'M':[],
    'N':[]

}

def dfs(graph, start_node):
    visited = set()
    stack = []
    stack.append(start_node)

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node, end=' ')
            for child in reversed(graph[node]):
                if child not in visited:
                    stack.append(child)

dfs(graph,'A')