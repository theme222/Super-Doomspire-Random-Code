# Super-Doomspire-Random-Code
run the code and the challenge will be there plus everything else
ALSO I'm A TERRIBLE PROGRAMMER SO DON'T EXPECT ANYTHING FANCY IN HERE JUST RUN THE CODE AND YOU'll BE FINE
if you wanna change anything you can if you wanna I'll prob not update this tho
this is made in python 3.8 i think so yea you might wanna download that
but if you don't wanna download you can just copy this into https://repl.it/languages/python3 fun fact I made this during class

---------copy underneath this line----------------
from random import choice

weaponslotlist = []
rocketlist = ['Rocket Launcher', 'Scope Shot', 'Starblaster', 'Shadow Dragon', 'Hoss Hog', 'Arm Cannon', 'Rock Star','Laser Cannon', 'Crystal Blaster']
swordlist = ["normal", "fire", "bigboi", "homerunner", 'tennis', 'brick', "vox", "pan", "ice", "shadow", "heart"]
bomblist = ['Bomb', 'Square Bomb', 'Remote Detonator', 'Shadow Bomb', 'Sticky Bomb']
balllist = ['Superball', 'Coconut', 'Boomerang', 'Hat-A-Rang', 'Lava Ball', 'Shadow Shuriken', 'Snowball','Paintball Gun', 'Slingshot', 'Bow']
trowellist = ['Trowel', 'Truss Trowel', 'Spike Trowel', 'Bridge Trowel', 'Ball Turret', 'Cage Trowel', 'Shadow Clone','Trampoline Trowel']
extraeventlist = ['bombonly', 'rocketonly', 'nosword', 'notrowel+ball', 'nowalking', "don'ttakedamage"]
lolhaha = ["weapon", 'bomb', 'sword', 'ball', 'trowel']
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
