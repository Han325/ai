class Node:
    def __init__(self, vacuum="left", leftdirt=0, rightdirt=0, parent=None, action=None):
        self.vacuum = vacuum  # Left/right
        self.leftdirt = leftdirt  # 0/1
        self.rightdirt = rightdirt  # 0/1
        self.parent = parent
        self.action = action

    def __repr__(self):
        return f"({self.vacuum}, {self.leftdirt}, {self.rightdirt}, Action: {self.action})"

def transitionmodel(node, action):
    new_vacuum = node.vacuum
    new_leftdirt = node.leftdirt
    new_rightdirt = node.rightdirt
    if action == 'left':
        new_vacuum = 'left'
    elif action == 'right':
        new_vacuum = 'right'
    elif action == 'suck':
        if new_vacuum == 'left':
            new_leftdirt = 0
        else:
            new_rightdirt = 0

    return Node(vacuum=new_vacuum, leftdirt=new_leftdirt, rightdirt=new_rightdirt, parent=node, action=action)

def isgoal(node):
    return node.leftdirt == 0 and node.rightdirt == 0

def isnodeinlist(node, listtocheck):
    return any(n.vacuum == node.vacuum and n.leftdirt == node.leftdirt and n.rightdirt == node.rightdirt for n in listtocheck)

def trace_path(node):
    """Traces back from the goal node to the initial node to capture the path."""
    path = []
    while node.action is not None:  # initial node's action is None
        path.insert(0, node.action)
        node = node.parent
    return path

def bfs(initial_node):
    frontier = [initial_node]
    explored = []
    actions = ['left', 'right', 'suck']

    while frontier:
        current_node = frontier.pop(0)

        if isgoal(current_node):
            return trace_path(current_node)

        explored.append(current_node)

        for action in actions:
            child = transitionmodel(current_node, action)
            if not isnodeinlist(child, explored) and not isnodeinlist(child, frontier):
                frontier.append(child)
    
    return None  # if no solution is found

# Initialize and execute
initial = Node(vacuum="left", leftdirt=1, rightdirt=1)
solution = bfs(initial)

if solution:
    print("Solution found!")
    print("Sequence of actions to goal:", solution)
else:
    print("No solution found.")
