import pygame
import colFont
import gameBoard



def MousePos():
    pos = pygame.mouse.get_pos()
    posX,posY = pygame.mouse.get_pos()
    Mousexy = colFont.arial21.render("X: "+str(posX) + " " + "Y: " + str(posY), True, colFont.green)
    gameBoard.screen.blit(Mousexy, (505, 15))