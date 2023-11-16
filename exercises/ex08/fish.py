"""File to define Fish class."""


class Fish:
    """Fishies."""
    age: int
    
    def __init__(self, age=0):
        """Setting base __init__."""
        self.age = age
        return None
    
    def one_day(self):
        """One day for the fishes."""
        self.age += 1
        return None