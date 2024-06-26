
import random
dice = [1, 2, 3, 4, 5, 6]

def dice_roll ():
    dice_roller = random.choice(dice)
    return dice_roller

print(dice_roll())