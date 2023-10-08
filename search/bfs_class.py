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
  def __init__(self, state=None, parent=None):
    self.state = state
    self.parent = parent
    self.children = []

  def addChildren(self, children):
    self.children.extend(children)

def expandAndReturnChildren(state_space, node):
  children = []
  for [m,n,c] in state_space:
    if m == node.state:
      children.append(Node(n, node.state))
    elif n == node.state:
      children.append(Node(m, node.state))
  return children

def bfs(state_space, initial_state, goal_state):
  frontier = []
  explored = []
  found_goal = False
  goalie = Node()
  solution = []
  # add initial state to frontier
  frontier.append(Node(initial_state, None))

  while not found_goal:
    # expand the first in the frontier
    children = expandAndReturnChildren(state_space, frontier[0])
    # add children list to the expanded node
    frontier[0].addChildren(children)
    # add to the explored list
    explored.append(frontier[0])
    # remove the expanded frontier
    del frontier[0]
    # add children to the frontier
    for child in children:
      # check if a node was expanded or generated previously
      if not (child.state in [e.state for e in explored]) and not (child.state in [f.state for f in frontier]):
        # goal test
        if child.state == goal_state:
          found_goal = True
          goalie = child
        frontier.append(child)
    print("Explored:", [e.state for e in explored])
    print("Frontier:", [f.state for f in frontier])
    print("Children:", [c.state for c in children])
    print("")

  solution = [goalie.state]
  path_cost = 0
  while goalie.parent is not None:
    solution.insert(0, goalie.parent)
    for e in explored:
      if e.state == goalie.parent:
        path_cost += getCost(state_space, e.state, goalie.state)
        goalie = e
        break
  return solution, path_cost

def getCost(state_space, state0, state1):
  for [m,n,c] in state_space:
    if [state0,state1] == [m,n] or [state1,state0] == [m,n]:
      return c


[solution, cost] = bfs(state_space, initial_state, goal_state)
print("Solution:", solution)
print("Path Cost:", cost)