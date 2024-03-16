import random

class Environment(object):
    def __init__(self):
        self.locationCondition = {'A': '1', 'B': '1', 'C': '1', 'D': '1'}
        self.locationCondition['A'] = str(random.choice([0, 1]))
        self.locationCondition['B'] = str(random.choice([0, 1]))
        self.locationCondition['C'] = str(random.choice([0, 1]))
        self.locationCondition['D'] = str(random.choice([0, 1]))

    def get_accuracy(self):
        correct_placements = sum(1 for loc in self.locationCondition if
                                 self.locationCondition[loc] == '1' and self.locationCondition[loc] != '0')
        total_placements = len(self.locationCondition)
        return correct_placements / total_placements

class SRAg(Environment):
    def __init__(self):
        super().__init__()
        self.vaccum_placements = 0
        self.correct_placements = 0

    def clean(self):
        locations = [0, 1, 2, 3]
        vaccumLocation = random.choice(locations)
        self.vaccum_placements += 1
        if vaccumLocation == 0 and self.locationCondition['A'] == '1':
            self.correct_placements += 1
            self.locationCondition['A'] = '0'
            print('Location A is dirty, vacuum is placed at A, Location A is clean')
        elif vaccumLocation == 1 and self.locationCondition['B'] == '1':
            self.correct_placements += 1
            self.locationCondition['B'] = '0'
            print('Location B is dirty, vacuum is placed at B, Location B is clean')
        elif vaccumLocation == 2 and self.locationCondition['C'] == '1':
            self.correct_placements += 1
            self.locationCondition['C'] = '0'
            print('Location C is dirty, vacuum is placed at C, Location C is clean')
        elif vaccumLocation == 3 and self.locationCondition['D'] == '1':
            self.correct_placements += 1
            self.locationCondition['D'] = '0'
            print('Location D is dirty, vacuum is placed at D, Location D is clean')
        else:
            print(f'Vacuum is placed at {vaccumLocation}, but that location is already clean')
        print(f'Accuracy: {self.get_accuracy() * 100:.2f}%')

agent = SRAg()
agent.clean()