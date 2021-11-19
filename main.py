import Combat
import pygame
import Initiative
import colFont
import gameBoard
import drawPlayer
import Mouse
import Button


pygame.init()
startWar = Button.myButton((0, 255, 0), 450, 400, 250, 100, colFont.arial21, 'Start War!')
running = True

while running:
    for event in pygame.event.get():
        Mouse.MousePos()
        if event.type == pygame.QUIT:
            running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if startWar.isOver(Mouse.pos):
                    if Mouse.pos[0] and wardeclared == 0:
                        startWar.color = (25, 100, 170)
                        startWar.text = "Pause War"
                        wardeclared = 1
                        Initiative.initiative.gameState=0

                    elif Mouse.pos[0] and wardeclared == 1:
                        startWar.color = (0, 255, 0)
                        startWar.text = "Start War"
                        wardeclared = 0
                        Initiative.initiative.gameState=10
                    elif Mouse.pos[0] and wardeclared ==1:
                        Initiative.initiative.gameState=1

        if Initiative.initiative.gameState !=10:
            if Initiative.initiative.gameState == 0:
                Initiative.rollInitiative()
            if Initiative.initiative.gameState == 1:
                Combat.rollAction()
            if Initiative.initiative.gameState==2:
                Combat.resolveAttack()
            if drawPlayer.RedUnit.dead == 1:
                Combat.redPlayerReset()
                Initiative.initiative.gameState = 1
            elif drawPlayer.BlueUnit.dead == 1:
                Combat.bluePlayerReset()
                Initiative.initiative.gameState = 1
            else:
                Initiative.initiative.gameState = 1
        gameBoard.drawGameBoard()

        drawPlayer.DrawPlayer()

        pygame.display.flip()

pygame.quit()
