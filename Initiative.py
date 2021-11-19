import UnitStats
import colFont
import drawPlayer
import random


class initiative():
    gameState = 0


def rollInitiative():
    drawPlayer.RedUnit.initiative = random.randint(1, 10)
    drawPlayer.BlueUnit.initiative = random.randint(1, 10)
    checkInit()


def checkInit():
    if drawPlayer.RedUnit.initiative > drawPlayer.BlueUnit.initiative:
        drawPlayer.RedUnit.initWin = 1
        initiative.gameState= 1
        drawPlayer.DrawPlayer()

    elif drawPlayer.RedUnit.initiative == drawPlayer.BlueUnit.initiative:
       rollInitiative()

    else:
        drawPlayer.BlueUnit.initWin = 1
        initiative.gameState= 1
        drawPlayer.DrawPlayer()


def rerollInit():
    value =1