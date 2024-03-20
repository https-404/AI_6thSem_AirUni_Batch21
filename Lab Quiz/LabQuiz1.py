from simpleai.search import SearchProblem, astar

# Define your graph as a dictionary of nodes and their neighbors
graph = {
    'A': {'B': 1, 'E': 3},
    'B': {'A': 2, 'G': 9},
    'C': {'B': 3},
    'D': {'G': 1,  'E': 6},
    'E': {'D': 6, 'A': 3},
    'G' : {'D': 1 , 'B': 9}
}

# Define your search problem
class Quiz1_210894(SearchProblem):
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state

    def actions(self, state):
        return list(graph[state].keys())

    def result(self, state, action):
        return action

    def cost(self, state, action, state2):
        return graph[state][state2]

    def is_goal(self, state):
        return state == self.goal_state

# Create an instance of the search problem
problem = Quiz1_210894('A', 'G')

# Run A* search algorithm
result = astar(problem)

# Print the path from initial state to goal state
print('Path:', result.path())
print('Cost:', result.cost)