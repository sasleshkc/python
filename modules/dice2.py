import random
class Dice:
    def randomnumbers(self):
        first=random.randint(1,6)
        second=random.randint(1,6)
        return first,second
dice1=Dice()
print(dice1.randomnumbers())


