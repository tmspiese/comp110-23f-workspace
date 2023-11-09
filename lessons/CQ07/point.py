"""Creating Point."""

from __future__ import annotations

__author__ = "730684472"


class Point:
    """Class Point with x and y attributes."""
    x: float
    y: float

    def __init__(self, x_init: float = 0, y_init: float = 0):
        """Constructor."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """Scale Point class by factor."""
        self.x = self.x * factor 
        self.y = self.y * factor 

    def scale(self, factor: int) -> Point:
        """Create new point with Point values multiplied by factor."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point
    
    def __str__(self) -> str:
        """Prints x and y values."""
        return (f"x: {self.x}; y: {self.y}")
    
    def __mul__(self, factor: int | float) -> Point:
        """Prints x and y multiplied by factor."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point
    
    def __add__(self, factor: int | float) -> Point:
        """Prints x and y added to factor."""
        my_point: Point = Point(self.x + factor, self.y + factor)
        return my_point