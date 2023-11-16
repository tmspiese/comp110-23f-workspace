"""File to define Bear class."""


class Bear:
    """Bear class."""

    age: int
    hunger_score: int
    
    def __init__(self, age=0, hs=0):
        """Setting base __init__."""
        self.age = age
        self.hunger_score = hs

        return None
    
    def one_day(self):
        """One day in a bears shoes."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """Bear be eatting."""
        self.hunger_score += num_fish 