import pygame
import sys

window = pygame.display.set_mode((920, 720))
pygame.display.set_caption(u"Hahki")
pygame.display.set_icon(pygame.image.load('pic\DBlack.gif').convert())
mainscreen = pygame.Surface((720, 720))
rightscreen = pygame.Surface((280, 720))

pygame.font.init()
font = pygame.font.SysFont("monospace", 50)

labalWin = font.render("Победа", 1, (255, 0, 0))
labelLose = font.render("Проигрышь", 1, (0, 0, 0))


class EndMenu:
    def __init__(self):
        super().__init__()
        self.i_menu = pygame.image.load('pic\menu.png')
        self.i_rmenu = pygame.image.load('pic\menurightscreen.png')


    def run(self, ishod):
        done = True

        label = labalWin
        if ishod == "lose":
            label = labelLose

        while done:
            window.blit(mainscreen, (0, 0))
            window.blit(rightscreen, (720, 0))
            mainscreen.blit(self.i_menu, (0, 0))
            mainscreen.blit(label, (330, 200))
            rightscreen.blit(self.i_rmenu, (0, 0))
            pygame.display.flip()
