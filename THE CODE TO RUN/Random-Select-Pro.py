# btw this is the hard mode with extra hard stuff and might require some progress in the game
# if you want it easy just run the other file this is basically chaos
# made by theme222
# https://github.com/theme222/Super-Doomspire-Random-Code
# the main difference is that the extra events are much harder also some weapons are removed

from random import choice, randint

weaponslotlist = []
rocketlist = ['Scope Shot', 'Starblaster', 'Shadow Dragon', 'Hoss Hog', 'Arm Cannon', 'Rock Star',
              'Laser Cannon']
swordlist = ["fire sword", "greatsword", "homerunner", 'tennis', 'brick breaker', "voxcalliber", "frying pan",
             "ice sword", "darkheart"]
bomblist = ['Bomb', 'Square Bomb', 'Shadow Bomb', 'Sticky Bomb']
balllist = ['Coconut', 'Boomerang', 'Hat-A-Rang', 'Lava Ball', 'Snowball',
            'Paintball Gun', 'Slingshot', 'Bow']
trowellist = ['Trowel', 'Truss Trowel', 'Spike Trowel', 'Bridge Trowel', 'Cage Trowel', 'Shadow Clone',
              'Trampoline Trowel']
extraeventlist = ['bomb only', 'no special abilities', "play on a different console than you're used to",
                  "every time you change weapons do the most annoying emote",
                  "play while you have a menu open", "no throwable weapons", "no projectile shooting weapons",
                  "every time you use an ability you have to type the weapon name in chat",
                  "you can't do anything until you have no spawns", "don't take damage",
                  "change your view perspective every time you die", 'no walking',
                  'every time you die you have to reset again']
lolhaha = ["rocket", 'bomb', 'sword', 'ball', 'trowel']
wincondition = ['get {e} kills'.format(e=randint(8, 12)), 'win twice in a row', ' get more kills than bricks',
                'get more than {e} bricks'.format(e=randint(150, 250)),
                'win in 4 minutes']

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
