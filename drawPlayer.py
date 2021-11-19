import drawPlayer
import gameBoard
import colFont
import UnitStats
import pygame


RedUnit = UnitStats.BasicUnit(100, 0, 0, 0, True, 0, 0, False, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0)
BlueUnit = UnitStats.BasicUnit(100, 0, 0, 0, True, 0, 0, False, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0)

def DrawPlayer():
    redName = colFont.arial21.render('Red', True, colFont.red)
    blueName = colFont.arial21.render('Blue', True, colFont.blue)

    redUnitLife = colFont.arial21.render('Life: ' + str(RedUnit.life), True, colFont.red)
    blueUnitLife = colFont.arial21.render('Life: ' + str(BlueUnit.life), True, colFont.blue)

    redUnitAttack = colFont.arial21.render('Attack: ' + str(RedUnit.attack), True, colFont.red)
    blueUnitAttack = colFont.arial21.render('Attack: ' + str(BlueUnit.attack), True, colFont.blue)

    redUnitDefense = colFont.arial21.render('Defense: ' + str(RedUnit.defend), True, colFont.red)
    blueUnitDefense = colFont.arial21.render('Defense: ' + str(BlueUnit.defend), True, colFont.blue)

    redUnitInitibative = colFont.arial21.render('Initiative: ' + str(RedUnit.initiative), True, colFont.red)
    blueUnitInitiative = colFont.arial21.render('Initiative: ' + str(BlueUnit.initiative), True, colFont.blue)

    redWin = colFont.arial21.render('Red Win: ' + str(RedUnit.totwin), True, colFont.red)
    blueWin = colFont.arial21.render('Blue wins: ' + str(BlueUnit.totwin), True, colFont.blue)

    redLoss = colFont.arial21.render('Red Loss: ' + str(RedUnit.totloss), True, colFont.red)
    blueLoss = colFont.arial21.render('Blue Loss: ' + str(BlueUnit.totloss), True, colFont.blue)

    redBigWin = colFont.arial42.render ('', True, (255, 0, 0))
    blueBigWin = colFont.arial42.render('', True, (255, 0, 0))

    redDefendRoll = colFont.arial21.render(str(RedUnit.defendRoll), True, colFont.yellow)
    redDefend = colFont.arial21.render(str(RedUnit.defend), True, colFont.yellow)
    redDefendTotal = colFont.arial21.render( str(RedUnit.totalDefense), True, colFont.yellow)

    redAttackRoll = colFont.arial21.render(str(RedUnit.attackRoll), True, colFont.yellow)
    redAttack = colFont.arial21.render(str(RedUnit.attack), True, colFont.yellow)
    redAttackTotal = colFont.arial21.render( str(RedUnit.totalAttack), True, colFont.yellow)

    blueDefendRoll = colFont.arial21.render(str(BlueUnit.defendRoll), True, colFont.yellow)
    blueDefend = colFont.arial21.render(str(BlueUnit.defend), True, colFont.yellow)
    blueDefendTotal = colFont.arial21.render(str(BlueUnit.totalDefense), True, colFont.yellow)

    blueAttackRoll = colFont.arial21.render(str(BlueUnit.attackRoll), True, colFont.yellow)
    blueAttack = colFont.arial21.render(str(BlueUnit.attack), True, colFont.yellow)
    blueAttackTotal = colFont.arial21.render( str(BlueUnit.totalAttack), True, colFont.yellow)

    redOffense = colFont.arial21.render("Offensive", True, colFont.red)
    blueOffense = colFont.arial21.render("Offensive", True, colFont.blue)


    redDefense = colFont.arial21.render("Defensive", True, colFont.red)
    blueDefense = colFont.arial21.render("Defensive", True, colFont.blue)

    yellowBigPlus = colFont.arial42.render("+", True, colFont.yellow)
    yellowBigEqual = colFont.arial42.render("=", True, colFont.yellow)

    redattackstr = colFont.arial21.render("BlueUnit   Defend    Total    ", True, colFont.red)
    blueattackstr = colFont.arial21.render("Red Unit   Attack     Total    ", True, colFont.blue)

    redattackstr2 = colFont.arial21.render("Attack        Roll     Attack ", True, colFont.red)
    blueattackstr2 = colFont.arial21.render("Attack       Roll      Attack ", True, colFont.blue)

    reddefensestr = colFont.arial21.render("Red Unit   Defend    Total    ", True, colFont.red)
    bluedefensestr = colFont.arial21.render("Blue Unit   Defend    Total    ", True, colFont.blue)

    reddefensestr2 = colFont.arial21.render(" Defend     Roll      Defend ", True, colFont.red)
    bluedefensestr2 = colFont.arial21.render("Defend       Roll      Defend ", True, colFont.blue)

    redAttackSuccess = colFont.arial21.render("Attack Successful", True, colFont.red)
    blueAttackSuccess = colFont.arial21.render("Attack Successful", True, colFont.blue)

    redDefendSuccess = colFont.arial21.render("Defend Successful", True, colFont.red)
    blueDefendSuccess = colFont.arial21.render("Defend Successful", True, colFont.blue)

    redTotalDamage = colFont.arial21.render(str(RedUnit.totalDamage) , True, colFont.yellow)
    blueTotalDamage = colFont.arial21.render(str(BlueUnit.totalDamage) , True, colFont.yellow)

    redDamageStr1 = colFont.arial21.render("Damage  Damage   Total ", True, colFont.red)
    redDamageStr2 = colFont.arial21.render("  Base       Roll     Damage ", True, colFont.red)

    blueDamageStr1 = colFont.arial21.render(" Damage  Damage    Total ", True, colFont.blue)
    blueDamageStr2 = colFont.arial21.render("  Base        Roll     Damage ", True, colFont.blue)

    redDamageBase = colFont.arial21.render(str(RedUnit.damage) , True, colFont.yellow)
    blueDamageBase = colFont.arial21.render(str(BlueUnit.damage) , True, colFont.yellow)

    redDamageRoll = colFont.arial21.render(str(RedUnit.rollDamage) , True, colFont.yellow)
    blueDamageRoll = colFont.arial21.render(str(BlueUnit.rollDamage) , True, colFont.yellow)

    blueUnitDies = colFont.arial21.render("Blue Unit Is Destroyed" , True, colFont.blue)
    redUnitDies = colFont.arial21.render("Red Unit Is Destroyed", True, colFont.red)
    if RedUnit.initWin == 1:
        pygame.draw.rect(gameBoard.screen, (255, 255, 255), (25, 105, 155, 18), 0)
        pygame.draw.rect(gameBoard.screen, (255, 255, 255), (330, 50, 115, 20), 0)
        pygame.draw.rect(gameBoard.screen, (255, 255, 255), (690, 50, 118, 20), 0)

        gameBoard.screen.blit(redAttackRoll, (280, 140))
        gameBoard.screen.blit(yellowBigPlus, (330, 130))
        gameBoard.screen.blit(redAttack, (390, 140))
        gameBoard.screen.blit(yellowBigEqual, (460, 130))
        gameBoard.screen.blit(redAttackTotal, (500, 140))

        gameBoard.screen.blit(redOffense, (330, 50))
        gameBoard.screen.blit(redattackstr, (250, 100))
        gameBoard.screen.blit(redattackstr2, (255, 120))

        gameBoard.screen.blit(blueDefense, (690, 50))
        gameBoard.screen.blit(bluedefensestr, (615, 100))
        gameBoard.screen.blit(bluedefensestr2, (620, 120))
        gameBoard.screen.blit(blueDefend, (650, 140))
        gameBoard.screen.blit(yellowBigPlus, (700, 135))
        gameBoard.screen.blit(blueDefendRoll, (770, 140))
        gameBoard.screen.blit(yellowBigEqual, (815, 130))
        gameBoard.screen.blit(blueDefendTotal, (880, 140))
        if RedUnit.attackSuccess == 1:
            pygame.draw.rect(gameBoard.screen, (255, 255, 255), (300, 180, 215, 18), 0)
            gameBoard.screen.blit(redAttackSuccess, (300, 180))
            gameBoard.screen.blit(redDamageStr1, (260, 200))
            gameBoard.screen.blit(redDamageStr2, (260, 220))
            gameBoard.screen.blit(redDamageBase, (285, 240))
            gameBoard.screen.blit(yellowBigPlus, (350, 230))
            gameBoard.screen.blit(redDamageRoll, (405, 240))
            gameBoard.screen.blit(yellowBigEqual, (450, 230))
            gameBoard.screen.blit(redTotalDamage, (500, 240))
            if BlueUnit.dead==1:
                gameBoard.screen.blit(blueUnitDies, (600, 240))

        else:
            pygame.draw.rect(gameBoard.screen, (255, 255, 255), (660, 180, 215, 18), 0)
            gameBoard.screen.blit(blueDefendSuccess, (660, 180))

    if BlueUnit.initWin == 1:
        pygame.draw.rect(gameBoard.screen, (255, 255, 255), (1030, 105, 155, 18), 0)
        pygame.draw.rect(gameBoard.screen, (255, 255, 255), (330, 50, 115, 20), 0)
        pygame.draw.rect(gameBoard.screen, (255, 255, 255), (690, 50, 118, 20), 0)

        gameBoard.screen.blit(blueAttackRoll, (640, 140))
        gameBoard.screen.blit(yellowBigPlus, (700, 135))
        gameBoard.screen.blit(blueAttack, (750, 140))
        gameBoard.screen.blit(yellowBigEqual, (815, 130))
        gameBoard.screen.blit(blueAttackTotal, (865, 140))

        gameBoard.screen.blit(blueOffense, (690, 50))
        gameBoard.screen.blit(blueattackstr, (615, 100))
        gameBoard.screen.blit(blueattackstr2, (620, 120))

        gameBoard.screen.blit(redDefense, (330, 50))
        gameBoard.screen.blit(reddefensestr, (250, 100))
        gameBoard.screen.blit(reddefensestr2, (250, 120))

        gameBoard.screen.blit(redDefend, (280, 140))
        gameBoard.screen.blit(yellowBigPlus, (330, 135))
        gameBoard.screen.blit(redDefendRoll, (390, 140))
        gameBoard.screen.blit(yellowBigEqual, (450, 130))
        gameBoard.screen.blit(redDefendTotal, (510, 140))
        if BlueUnit.attackSuccess == 1:
            pygame.draw.rect(gameBoard.screen, (255, 255, 255), (660, 180, 215, 18), 0)
            gameBoard.screen.blit(blueAttackSuccess, (660, 180))
            gameBoard.screen.blit(blueDamageStr1, (600, 200))
            gameBoard.screen.blit(blueDamageStr2, (600, 220))
            gameBoard.screen.blit(blueDamageBase, (630, 240))
            gameBoard.screen.blit(yellowBigPlus, (690, 230))
            gameBoard.screen.blit(blueDamageRoll, (750, 240))
            gameBoard.screen.blit(yellowBigEqual, (800, 230))
            gameBoard.screen.blit(blueTotalDamage, (860, 240))
            if RedUnit.dead==1:
                gameBoard.screen.blit(redUnitDies, (600, 240))
        else:
            pygame.draw.rect(gameBoard.screen, (255, 255, 255), (305, 180, 225, 18), 0)
            gameBoard.screen.blit(redDefendSuccess, (310, 180))


    gameBoard.screen.blit(redName, (25, 25))
    gameBoard.screen.blit(blueName, (1050, 25))

    gameBoard.screen.blit(redUnitLife, (25, 45))
    gameBoard.screen.blit(blueUnitLife, (1030, 45))

    gameBoard.screen.blit(redUnitAttack, (25, 65))
    gameBoard.screen.blit(blueUnitAttack, (1030, 65))

    gameBoard.screen.blit(redUnitDefense, (25, 85))
    gameBoard.screen.blit(blueUnitDefense, (1030, 85))

    gameBoard.screen.blit(redUnitInitibative, (25, 105))
    gameBoard.screen.blit(blueUnitInitiative, (1030, 105))

    gameBoard.screen.blit(redWin, (330, 75))
    gameBoard.screen.blit(blueWin, (670, 75))

    gameBoard.screen.blit(redLoss, (25, 125))
    gameBoard.screen.blit(blueLoss, (1030, 125))

    gameBoard.screen.blit(redBigWin, (525, 145))
    gameBoard.screen.blit(blueBigWin, (815, 145))

    #gameBoard.screen.blit(redattackstr, (275, 100))

    #gameBoard.screen.blit(redattackstr2, (285, 120))

    #gameBoard.screen.blit(redbigPlus, (378, 100))

    #gameBoard.screen.blit(redbigEqual, (475, 100))







    #gameBoard.screen.blit(redattackstr, (615, 100))
    #gameBoard.screen.blit(redattackstr2, (615, 120))
    ##gameBoard.screen.blit(bluebigPlus, (718, 100))
    #gameBoard.screen.blit(bluebigEqual, (818, 100))