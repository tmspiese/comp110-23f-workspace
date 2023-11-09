"""Testing point.py file."""

__author__ = "730684472"

from lessons.CQ07.point import Point

my_point: Point = Point(2.5, 3.5)

my_point_scale: Point = my_point.scale(2)
print(my_point_scale.x)
print(my_point_scale.y)
my_point = my_point.scale_by(3)
print(my_point)
