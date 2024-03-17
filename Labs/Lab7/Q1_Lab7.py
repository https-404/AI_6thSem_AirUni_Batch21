from simpleai.search import SearchProblem, astar

graph_states = {
    1: ('ACB', '', ''),
    2: ('A', 'CB', ''),
    3: ('BA', 'C', ''),
    4: ('CBA', '', ''),
    5: ('BCA', '', ''),
    6: ('CA', 'B', ''),
    7: ('A', 'B', 'C'),
    8: ('A', 'BC', ''),
    9: ('ABC', '', ''),
    10: ('CAB', '', ''),
    11: ('AB', 'C', ''),
    12: ('B', 'AC', ''),
    13: ('BAC', '', '')
}


AdjecencyInfo = {
    1: [2],
    2: [1, 6, 7],
    3: [4, 7, 8],
    4: [3],
    5: [6],
    6: [5, 2, 7],
    7: [2, 3, 6, 8, 11, 12],
    8: [3, 7, 9],
    9: [8],
    10: [11],
    11: [7, 10, 12],
    12: [11, 7, 13],
    13: [12]
}

class QueueProblem(SearchProblem):
    def __init__(self, initial_state, goal_state, AdjecencyInfo):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.AdjecencyInfo = AdjecencyInfo
        super().__init__(initial_state)

    def actions(self, state):
        statesDictKeys = graph_states.keys()
        statesDictValues = graph_states.values()
        currentStateIndex = list(statesDictValues).index(state) 
        current_state_key = list(statesDictKeys)[currentStateIndex] 

        return [(current_state_key, next_state) for next_state in self.AdjecencyInfo[current_state_key]]

    def result(self, state, action):
        return graph_states[action[1]]

    def is_goal(self, state):
        return state == self.goal_state

    def heuristic(self, state):
        misplaced_blocks = sum(1 for block in state[0] if block != 'A' and block != 'C')
        return misplaced_blocks

    def cost(self, state, action, state2):
        return 1

def main():
    initial_state = graph_states[6]
    final_state = graph_states[9] 
    problem = QueueProblem(initial_state, final_state, AdjecencyInfo)
    result = astar(problem)

    if result:
        print("Path found:")
        for action, state in result.path():
            print(f"Action: {action}, State: {state}")

        print(f"\nNet Cost: {result.cost}")
    else:
        print("No path found")

if __name__ == "__main__":
    main()
