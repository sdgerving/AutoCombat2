import Initiative
import drawPlayer
import random

temp = 0
def rollAction():

    if drawPlayer.RedUnit.initWin==1:
        drawPlayer.RedUnit.attackRoll= rollAttack(1,20)
        drawPlayer.RedUnit.totalAttack = drawPlayer.RedUnit.attack + drawPlayer.RedUnit.attackRoll
        drawPlayer.BlueUnit.defendRoll= rollAttack(1,20)
        drawPlayer.BlueUnit.totalDefense = drawPlayer.BlueUnit.defend + drawPlayer.BlueUnit.defendRoll
        Initiative.initiative.gameState = 2

    else:
        drawPlayer.BlueUnit.attackRoll= rollAttack(1,20)

        drawPlayer.BlueUnit.totalAttack = drawPlayer.BlueUnit.attack + drawPlayer.BlueUnit.attackRoll
        drawPlayer.RedUnit.defendRoll= rollAttack(1,20)
        drawPlayer.RedUnit.totalDefense = drawPlayer.RedUnit.defend + drawPlayer.RedUnit.defendRoll
        Initiative.initiative.gameState = 2

def rollAttack(x,y):
     return random.randint(x, y)


def resolveAttack():
    if drawPlayer.RedUnit.initWin == 1:
        if drawPlayer.RedUnit.totalAttack > drawPlayer.BlueUnit.totalDefense:
            drawPlayer.RedUnit.attackSuccess = 1
            drawPlayer.RedUnit.rollDamage = rollDamage(1,6)
            drawPlayer.RedUnit.totalDamage = drawPlayer.RedUnit.rollDamage + drawPlayer.RedUnit.damage
            drawPlayer.BlueUnit.life -= drawPlayer.RedUnit.totalDamage
            checkLife()
        else:
            drawPlayer.BlueUnit.defendSuccess = 1

    if drawPlayer.BlueUnit.initWin == 1:
        if drawPlayer.BlueUnit.totalAttack > drawPlayer.RedUnit.totalDefense:
            drawPlayer.BlueUnit.attackSuccess = 1
            drawPlayer.BlueUnit.rollDamage = rollDamage(1,6)
            drawPlayer.BlueUnit.totalDamage = drawPlayer.BlueUnit.rollDamage + drawPlayer.BlueUnit.damage
            drawPlayer.RedUnit.life -= drawPlayer.BlueUnit.totalDamage
            checkLife()
        else:
            drawPlayer.RedUnit.defendSuccess = 1


def rollDamage(x,y):
        return random.randint(x, y)

def checkLife():
    if drawPlayer.RedUnit.life <=0:
        drawPlayer.RedUnit.dead=1
    elif drawPlayer.BlueUnit.life <=0:
        drawPlayer.BlueUnit.dead=1

def redPlayerReset():
    drawPlayer.RedUnit.life = 100
    drawPlayer.RedUnit.attack = random.randint(1, 1000)
    drawPlayer.RedUnit.defend = random.randint(1, 1)
    drawPlayer.RedUnit.initiative = 0
    drawPlayer.RedUnit.attacker = 0
    drawPlayer.RedUnit.damage = 10
    drawPlayer.RedUnit.totwin = 0
    drawPlayer.RedUnit.totloss = 0
    drawPlayer.RedUnit.unitwin = 0
    drawPlayer.RedUnit.tempRoll = 0
    drawPlayer.RedUnit.totalAttack = 0
    drawPlayer.RedUnit.totalDefense = 0
    drawPlayer.RedUnit.hits = 0
    drawPlayer.RedUnit.initWin = 0
    drawPlayer.RedUnit.attackRoll = 0
    drawPlayer.RedUnit.defendRoll = 0
    drawPlayer.RedUnit.attackSuccess = 0
    drawPlayer.RedUnit.defendSuccess = 0
    drawPlayer.RedUnit.attackTie = 0
    drawPlayer.RedUnit.rollDamage = 0
    drawPlayer.RedUnit.totalDamage = 0
    drawPlayer.RedUnit.dead = 0

def bluePlayerReset():
    drawPlayer.BlueUnit.life = 100
    drawPlayer.BlueUnit.attack = random.randint(1, 1000)
    drawPlayer.BlueUnit.defend = random.randint(1, 1)
    drawPlayer.BlueUnit.initiative = 0
    drawPlayer.BlueUnit.attacker = 0
    drawPlayer.BlueUnit.damage = 10
    drawPlayer.BlueUnit.totwin = 0
    drawPlayer.BlueUnit.totloss = 0
    drawPlayer.BlueUnit.unitwin = 0
    drawPlayer.BlueUnit.tempRoll = 0
    drawPlayer.BlueUnit.totalAttack = 0
    drawPlayer.BlueUnit.totalDefense = 0
    drawPlayer.BlueUnit.hits = 0
    drawPlayer.BlueUnit.initWin = 0
    drawPlayer.BlueUnit.attackRoll = 0
    drawPlayer.BlueUnit.defendRoll = 0
    drawPlayer.BlueUnit.attackSuccess = 0
    drawPlayer.BlueUnit.defendSuccess = 0
    drawPlayer.BlueUnit.attackTie = 0
    drawPlayer.BlueUnit.rollDamage = 0
    drawPlayer.BlueUnit.totalDamage = 0
    drawPlayer.BlueUnit.dead = 0