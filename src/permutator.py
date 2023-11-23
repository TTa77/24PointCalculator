import queue
from itertools import permutations


class Permutator(object):
    def __init__(self, four_numbers: tuple):
        self.possible_sequence = queue.Queue()

        for i in permutations(four_numbers, 4):
            self.possible_sequence.put(i)

    def get_possible_sequence(self):
        return self.possible_sequence


