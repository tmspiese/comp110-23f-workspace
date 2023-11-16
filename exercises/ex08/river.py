"""File to define River class."""

__author__ = "730684472"

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear


class River:
    """The flowing river."""
    day: int
    bears: list[Bear]
    fish: list[Fish]
    
    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Checks age of all animals."""
        list_bear: list[Bear] = []
        list_fish: list[Fish] = []
        for elem in self.bears:
            if (elem.age <= 5):
                list_bear.append(elem)
        self.bears = list_bear
        for elem in self.fish:
            if (elem.age <= 3):
                list_fish.append(elem)
        self.fish = list_fish

        return None
    
    def remove_fish(self, amount: int):
        """Fishes die."""
        while (amount > 0):
            self.fish.pop(0)
            amount -= 1

    def bears_eating(self):
        """Bears gotta eat."""
        for elem in self.bears:
            if (len(self.fish) >= 5):
                self.remove_fish(3)
                elem.eat(3)
        return None
    
    def check_hunger(self):
        """Checking bears hunger."""
        list_bear: list[Bear] = []
        for elem in self.bears:
            if (elem.hunger_score < 0):
                list_bear.append(elem)
        self.bears = list_bear
        return None
        
    def repopulate_fish(self):
        """Fish making more fish."""
        offspring: list[Fish] = (len(self.fish) // 2) * 4
        for fish in range(offspring):
            self.fish.append(Fish())
        return None
    
    def repopulate_bears(self):
        """Bears making more bears."""
        offspring: list[Bear] = range(len(self.bears) // 2) 
        for bear in offspring:
            self.bears.append(Bear()) 
        return None
    
    def view_river(self):
        """A day at the river."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self) -> None:
        """One river week (7 days)."""
        for x in range(0, 7):
            self.one_river_day()