import pygame
import Button
import colFont

screen = pygame.display.set_mode([1200, 700])
startWar = Button.myButton((0, 255, 0), 450, 400, 250, 100, colFont.arial21, 'Start War!')

def drawGameBoard():
    screen.fill((0, 0, 20))
    pygame.draw.rect(screen, (255, 250, 250), (230, 0, 735, 500), 10)
    pygame.draw.rect(screen, (217, 24, 24), (0, 0, 225, 500), 8)
    pygame.draw.rect(screen, (12, 37, 145), (970, 0, 225, 500), 8)
    startWar.draw(screen, (0, 0, 0))
    # totalWins = colFont.arial21.render('Total number of fights: '+str(totalWins), True, (255,255,255))