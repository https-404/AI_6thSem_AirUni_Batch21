import random

class PacmanAgent:
    def __init__(self, grid_size, initial_state):
        self.grid_size = grid_size
        self.state = initial_state
        self.food_pallets = set()  # Positions of food pallets
        self.power_pallets = set()  # Positions of power pallets
        self.ghost_position = None

    def update_state(self, new_state):
        self.state = new_state

    def update_food_pallets(self, pallets):
        self.food_pallets = pallets

    def update_power_pallets(self, pallets):
        self.power_pallets = pallets

    def update_ghost_position(self, position):
        self.ghost_position = position

    def move(self, action):
        x, y = self.state
        if action == 'UP' and y > 0:
            self.state = (x, y - 1)
        elif action == 'DOWN' and y < self.grid_size - 1:
            self.state = (x, y + 1)
        elif action == 'LEFT' and x > 0:
            self.state = (x - 1, y)
        elif action == 'RIGHT' and x < self.grid_size - 1:
            self.state = (x + 1, y)

    def consume_food(self):
        if self.state in self.food_pallets:
            self.food_pallets.remove(self.state)
            return True
        return False

    def consume_power_pallet(self):
        if self.state in self.power_pallets:
            self.power_pallets.remove(self.state)
            return True
        return False

    def is_ghost_nearby(self):
        if abs(self.state[0] - self.ghost_position[0]) + abs(self.state[1] - self.ghost_position[1]) <= 1:
            return True
        return False

    def choose_action(self):
        possible_actions = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        return random.choice(possible_actions)

    def play(self):
        while self.food_pallets:
            action = self.choose_action()
            self.move(action)
            if self.consume_food():
                print("Pacman consumed food pallet at position:", self.state)
            if self.consume_power_pallet():
                print("Pacman consumed power pallet at position:", self.state)
            if self.is_ghost_nearby():
                print("Pacman encountered ghost!")
                # Take appropriate action to avoid the ghost


# Example usage:
grid_size = 4
initial_state = (0, 0)
pacman = PacmanAgent(grid_size, initial_state)
pacman.update_food_pallets({(1, 1), (2, 2), (3, 3)})
pacman.update_power_pallets({(0, 1)})
pacman.update_ghost_position((2, 0))

pacman.play()
