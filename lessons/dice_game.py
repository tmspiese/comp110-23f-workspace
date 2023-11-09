"""Randomly rolls dice and sums total."""

from random import randint

roll_1: int = randint (1,6)
roll_2: int = randint(1,6)
roll_3: int = randint(1,6)

dice_ind: int = 0
dice_sum: int = 0

dice_rolls: list[int] = [roll_1,roll_2,roll_3]

while(dice_ind <= len(dice_rolls)-1):
    print(dice_rolls[dice_ind])
    dice_sum += dice_rolls[dice_ind]
    dice_ind += 1

print(dice_sum)