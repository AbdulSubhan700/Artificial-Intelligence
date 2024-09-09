----------8 puzzle problem using A* Seach---------------

board = [[1, 2, 3], [5, 6, 0], [7, 8, 4]]
hn = {
    '1': {'goal_pos': (0, 0)},
    '2': {'goal_pos': (0, 1)},
    '3': {'goal_pos': (0, 2)},
    '4': {'goal_pos': (2, 2)},
    '5': {'goal_pos': (1, 0)},
    '6': {'goal_pos': (1, 2)},
    '7': {'goal_pos': (2, 1)},
    '8': {'goal_pos': (1, 1)},
    '0': {'goal_pos': (2, 0)}
}
def difference(goal, cur):
    return abs(goal[0]- cur[0]) + abs(goal[1] - cur[1])

def puzzle():
    queue=[]
    x_blank,y_blank=return_current_position(0)
    for key in hn:
        if key=='0':
            continue
        x, y = return_current_position(int(key))
        if hn[key]['goal_pos'] != (x, y):
           sp_dist=difference((x_blank,y_blank),(x,y))
           queue.append((key,sp_dist))
    if len(queue)!=0:
         queue.sort(key=lambda x: x[1])
         sorting_puzzle(queue) 
    else:
        print('Puzzle Solved')
        for row in board:
            for col in row:
                print(col,end=" ")
            print()    

def sorting_puzzle(queue):
    while queue:
        state,d=queue.pop(0)
        x_blank,y_blank=return_current_position(0)
        x,y=return_current_position(int(state))
        if difference((x,y),(x_blank,y_blank))==1:
            temp=board[x][y]
            board[x][y]=board[x_blank][y_blank]
            board[x_blank][y_blank]=temp
    puzzle()

def return_current_position(state):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == state:
                return i, j
# --------------------------------------------------------------------------------------------
print("PUZZLE")
for row in board:
    for col in row:
        print(col,end=" ")
    print() 
puzzle()

# -------------------A Star Search-------------------------------

def Astar(start_node, goal_node):
    
    # Estimated distances to the goal (heuristic)
    heuristic = {
        'Arad': 366, 'Bucharest': 0, 'Craiova': 160, 'Dobreta': 242, 'Eforie': 161, 'Fagaras': 176,
        'Giurgiu': 77, 'Hirsova': 151, 'Iasi': 226, 'Lugoj': 244, 'Mehadia': 241, 'Neamt': 234,
        'Oradea': 380, 'Pitesti': 10, 'Rimnicu Vilcea': 193, 'Sibiu': 253, 'Timisoara': 329,
        'Urziceni': 80, 'Vaslui': 199, 'Zerind': 374
    }

    # Map of cities and distances between them
    graph = {
        'Oradea': {'Zerind': 71, 'Sibiu': 151},
        'Zerind': {'Oradea': 71, 'Arad': 75},
        'Arad': {'Zerind': 75, 'Timisoara': 118, 'Sibiu': 140},
        'Sibiu': {'Oradea': 151, 'Arad': 140, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
        'Timisoara': {'Arad': 118, 'Lugoj': 111},
        'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
        'Mehadia': {'Lugoj': 70, 'Dobreta': 75},
        'Dobreta': {'Mehadia': 75, 'Craiova': 120},
        'Craiova': {'Dobreta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
        'Rimnicu Vilcea': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
        'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
        'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
        'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},
        'Giurgiu': {'Bucharest': 90},
        'Urziceni': {'Bucharest': 85, 'Hirsova': 98, 'Vaslui': 142},
        'Hirsova': {'Urziceni': 98, 'Eforie': 86},
        'Eforie': {'Hirsova': 86},
        'Vaslui': {'Urziceni': 142, 'Iasi': 92},
        'Iasi': {'Vaslui': 92, 'Neamt': 87},
        'Neamt': {'Iasi': 87},
    }

    # This checks if the start or goal node is not in the map
    if start_node not in graph or goal_node not in graph:
        print("Invalid node")
        return
    
    # A list to keep track of nodes to explore
    queue = [(heuristic[start_node], start_node)]
    
    # Distances from the start node to each node
    g_n = {node: float('inf') for node in graph}
    g_n[start_node] = 0
    
    visited = set()

    while queue:
        # Get the node with the lowest cost
        queue.sort()
        current_cost, node = queue.pop(0)

        if node in visited:
            continue

        visited.add(node)
        print(f"Visiting {node}")

        # If we've reached the goal, print the distance and stop
        if node == goal_node:
            print(f"Reached {goal_node}, Total Distance: {g_n[goal_node]}")
            return

        # Check all connected nodes
        for adjacent, distance in graph[node].items():
            if adjacent not in visited:
                new_cost = g_n[node] + distance
                if new_cost < g_n[adjacent]:
                    g_n[adjacent] = new_cost
                    queue.append((new_cost + heuristic[adjacent], adjacent))

# Example usage
Astar('Oradea', 'Bucharest')

# --------------Greedy Best First Search--------------------

def GBFS(start,end):
    distance=0
    queue=[]
    visited=set()
    queue.append((start,0)) #list of tuples including node and its weight like ('node',3)
    while queue:
        queue.sort(key=lambda x: x[1]) #sorting queue on basis of weight
        node,weight=queue.pop(0)
        distance+=weight
        
        if node not in visited:
            print(node,end=" --> ")
            visited.add(node)
        if node==end:
            print(f'\nDistance taken from {start} to {end} : {distance}')
            break
        for adjacent in graph[node]['Adjacents']:
            if adjacent not in visited:
                queue.append((adjacent,graph[node]['Adjacents'][adjacent]))
                
        
graph = {
        'Oradea': {'Adjacents': {'Zerind': 71, 'Sibiu': 151}},
        'Zerind': {'Adjacents': {'Oradea': 71, 'Arad': 75}},
        'Arad': {'Adjacents': {'Zerind': 75, 'Timisoara': 118, 'Sibiu': 140}},
        'Sibiu': {'Adjacents': {'Oradea': 151, 'Arad': 140, 'Fagaras': 99, 'Rimnicu Vilcea': 80}},
        'Timisoara': {'Adjacents': {'Arad': 118, 'Lugoj': 111}},
        'Lugoj': {'Adjacents': {'Timisoara': 111, 'Mehadia': 70}},
        'Mehadia': {'Adjacents': {'Lugoj': 70, 'Dobreta': 75}},
        'Dobreta': {'Adjacents': {'Mehadia': 75, 'Craiova': 120}},
        'Craiova': {'Adjacents': {'Dobreta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138}},
        'Rimnicu Vilcea': {'Adjacents': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97}},
        'Pitesti': {'Adjacents': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101}},
        'Fagaras': {'Adjacents': {'Sibiu': 99, 'Bucharest': 211}},
        'Bucharest': {'Adjacents': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85}},
        'Giurgiu': {'Adjacents': {'Bucharest': 90}},
        'Urziceni': {'Adjacents': {'Bucharest': 85, 'Hirsova': 98, 'Vaslui': 142}},
        'Hirsova': {'Adjacents': {'Urziceni': 98, 'Eforie': 86}},
        'Eforie': {'Adjacents': {'Hirsova': 86}},
        'Vaslui': {'Adjacents': {'Urziceni': 142, 'Iasi': 92}},
        'Iasi': {'Adjacents': {'Vaslui': 92, 'Neamt': 87}},
        'Neamt': {'Adjacents': {'Iasi': 87}},
    }
GBFS('Oradea','Sibiu')


