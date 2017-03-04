import random

class ForestService:
    def __init__(self, grow_probability: float, fire_probability: float):
        self.grow_probability = grow_probability
        self.fire_probability = fire_probability

    def should_grow_tree(self):
        if self.get_random_value() <= self.grow_probability:
            return True

        return False

    def should_start_fire(self):
        if self.get_random_value() <= self.fire_probability:
            return True

        return False

    def get_random_value(self):
        return random.random()