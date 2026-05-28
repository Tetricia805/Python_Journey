# program for producing random result pairs after rolling a dice twice using a class

import random


class Dice:
    def roll(self):
        first_roll = random.randint(1, 6)
        second_roll = random.randint(1, 6)
        return first_roll, second_roll


dice1 = Dice()
print(dice1.roll())

# or


class DiceNew:
    def roll1(self):
        sides = (1, 2, 3, 4, 5, 6)
        return random.randint(sides)


dice2 = DiceNew()
print(dice2.roll1())
