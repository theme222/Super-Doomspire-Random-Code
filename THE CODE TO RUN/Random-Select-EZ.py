# this is the easy one. Think it's easy? Try the pro one.
# made by theme222
# https://github.com/theme222/Super-Doomspire-Random-Code
from random import choice

weaponslotlist = []
rocketlist = ['Rocket Launcher', 'Scope Shot', 'Starblaster', 'Shadow Dragon', 'Hoss Hog', 'Arm Cannon', 'Rock Star',
              'Laser Cannon', 'Crystal Blaster']
swordlist = ["sword", "fire sword", "greatsword", "homerunner", 'tennis', 'brick breaker', "voxcalliber", "frying pan",
             "ice sword", "shadow blade", "darkheart"]
bomblist = ['Bomb', 'Square Bomb', 'Remote Detonator', 'Shadow Bomb', 'Sticky Bomb']
balllist = ['Superball', 'Coconut', 'Boomerang', 'Hat-A-Rang', 'Lava Ball', 'Shadow Shuriken', 'Snowball',
            'Paintball Gun', 'Slingshot', 'Bow']
trowellist = ['Trowel', 'Truss Trowel', 'Spike Trowel', 'Bridge Trowel', 'Ball Turret', 'Cage Trowel', 'Shadow Clone',
              'Trampoline Trowel']
extraeventlist = ['rocket only', 'no sword', 'no trowel+ball',  'normal',
                  'normal', 'no bomb jumps or rocket jumps', 'normal']
lolhaha = ["rocket", 'bomb', 'sword', 'ball', 'trowel']
wincondition = ['get 5 kills', 'win a game', 'get more than 50 bricks', "don't die"]

for i in range(1, 6):
    a = choice(lolhaha)
    lolhaha.remove(a)
    weaponslotlist.append(a)

print(weaponslotlist)
print("sword = ", choice(swordlist))
print("bomb = ", choice(bomblist))
print("rocket = ", choice(rocketlist))
print("ball = ", choice(balllist))
print("trowel = ", choice(trowellist))
print("challenge = ", choice(extraeventlist))
print("win condition = ", choice(wincondition))
print(" ")
print("if you don't have the specific weapon then change it to the default one")
