from queue import PriorityQueue

state_space = [
    ['Arad', 'Zerind', 75],
    ['Arad', 'Sibiu', 140],
    ['Arad', 'Timisoara', 118],
    ['Zerind', 'Oradea', 71],
    ['Oradea', 'Sibiu', 151],
    ['Timisoara', 'Lugoj', 111],
    ['Lugoj', 'Mehadia', 70],
    ['Mehadia', 'Drobeta', 75],
    ['Drobeta', 'Craiova', 120],
    ['Craiova', 'Rimnicu Vilcea', 146],
    ['Craiova', 'Pitesti', 138],
    ['Rimnicu Vilcea', 'Sibiu', 80],
    ['Rimnicu Vilcea', 'Pitesti', 97],
    ['Sibiu', 'Fagaras', 99],
    ['Fagaras', 'Bucharest', 211],
    ['Pitesti', 'Bucharest', 101],
    ['Bucharest', 'Giurgiu', 90],
    ['Bucharest', 'Urziceni', 85],
    ['Urziceni', 'Hirsova', 98],
    ['Urziceni', 'Vaslui', 142],
    ['Hirsova', 'Eforie', 86],
    ['Vaslui', 'Iasi', 92],
    ['Iasi', 'Neamt', 87]
]

initial_state = 'Arad'
goal_state = 'Bucharest'

class Node:
    def __init__(self, state, parent, cost=0):
        self.state = state
        self.parent = parent
        self.cost = cost

    def addChildren(self, children):
        self.children.extend(children)

def expandAndReturnChildren(state_space, node):
    children = []
    for [m,n,c] in state_space:
        if m == node.state:
            children.append(Node(n, node, c))
        elif n == node.state:
            children.append(Node(m, node, c))
    return children

def getCost(state_space, state0, state1):
    for [m,n,c] in state_space:
        if [state0, state1] == [m, n] or [state1, state0] == [m, n]:
            return c
    return 0

def ucs(state_space, initial_state, goal_state):
    frontier = PriorityQueue()
    explored = []

    frontier.put((0, Node(initial_state, None, 0)))

    while not frontier.empty():
        _, current_node = frontier.get()

        # Goal test during expansion
        if current_node.state == goal_state:
            path = []
            while current_node:
                path.insert(0, current_node.state)
                current_node = current_node.parent
            return path, getCost(state_space, path[-2], path[-1]) if len(path) > 1 else 0

        if current_node.state not in explored:
            explored.append(current_node.state)
            children = expandAndReturnChildren(state_space, current_node)

            for child in children:
                child_cost = current_node.cost + getCost(state_space, current_node.state, child.state)
                child.cost = child_cost
                if child.state not in [item[1].state for item in frontier.queue]:
                    frontier.put((child_cost, child))
                else:
                    # Replace with a lower-cost path in frontier if exists
                    for idx, (existing_cost, existing_node) in enumerate(frontier.queue):
                        if existing_node.state == child.state and existing_cost > child_cost:
                            frontier.queue[idx] = (child_cost, child)
                            break

    return [], 0

solution, cost = ucs(state_space, initial_state, goal_state)
print("Solution:", solution)
print("Path Cost:", cost)
