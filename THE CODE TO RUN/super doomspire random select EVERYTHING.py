# bruhhhhhhhhh look just please credit me thanks 
# maybe something along the lines of "made by theme" or something like that
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
extraeventlist = ['bombonly', 'rocketonly', 'nosword', 'notrowel+ball', 'nowalking', "don'ttakedamage"]
lolhaha = ["rocket", 'bomb', 'sword', 'ball', 'trowel']
wincondition = ['get 5 kills','win a game','get brick mvp']
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
print("challenge = ",choice(extraeventlist))
print("win condition = ",choice(wincondition))
