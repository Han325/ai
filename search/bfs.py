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

def expandAndReturnChildren(state_space, path_to_leaf_node):
  children = []
  for [m,n,c] in state_space:
    if m == path_to_leaf_node[-1]:
      children.append(path_to_leaf_node + [n])
    elif n == path_to_leaf_node[-1]:
      children.append(path_to_leaf_node + [m])
  return children


def bfs(state_space, initial_state, goal_state):
  frontier = []
  explored = []
  found_goal = False
  solution = []
  frontier.append([initial_state])
#   print("Initial frontier " + str([initial_state]))

  while not found_goal:
    # expand the first in the frontier
    children = expandAndReturnChildren(state_space, frontier[0])
    # copy the node to the explored set
    explored.append(frontier[0][-1])
    # remove the expanded frontier
    del frontier[0]
    # loop through the children
    for child in children:
      # check if a node was expanded or generated previously
      if not (child[-1] in explored) and not (child[-1] in [f[-1] for f in frontier]):
        # goal test
        if child[-1] == goal_state:
          found_goal = True
          solution = child
        # add children to the frontier
        frontier.append(child)
  return solution


print('Solution: ' + str(bfs(state_space, initial_state, goal_state)))
