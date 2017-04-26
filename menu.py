import pygame
import sys

from MenuSide import MenuSide

window = pygame.display.set_mode((920, 720))
pygame.display.set_caption(u"Hahki")
pygame.display.set_icon(pygame.image.load('pic/DBlack.gif').convert())
mainscreen = pygame.Surface((720, 720))
rightscreen = pygame.Surface((280, 720))


class Menu:

    game_type = "easy"
    game_side = "white"
    game_AI = 0

    done = True
    font_menu = pygame.font.SysFont("comicsansms", 50)
    punkt = 0

    def __init__(self, punkts):

        self.i_menu = pygame.image.load('pic/menu.png')
        self.i_rmenu = pygame.image.load('pic/menurightscreen.png')
        self.punkts = punkts

    def render(self, poverhnost, font, num_punkt):
        for e in self.punkts:
            if num_punkt == e[5]:
                poverhnost.blit(font.render(e[2], 1, e[4]), (e[0], e[1]))
            else:
                poverhnost.blit(font.render(e[2], 1, e[3]), (e[0], e[1]))

    def collaidePunkt(self, mp):
        for i in self.punkts:
            if mp[0] > i[0] and mp[0] < (i[0] + 155) and mp[1] > i[1] and mp[1] < (i[1] + 50):
                self.punkt = i[5]

    def doneWithPunkt(self):

        easy_game = 0
        AI_game = 1
        exit = 2

        if self.punkt == easy_game:
            self.done = False
            menuS = MenuSide()
            select = menuS.run()
            self.game_type = "easy"
            self.game_AI = 0
            self.game_side = select
            return self.game_type, self.game_AI, self.game_side



        if self.punkt == AI_game:
            pass

        elif self.punkt == exit:
            sys.exit()


    def run(self):

        while self.done:

            mp = pygame.mouse.get_pos()
            self.collaidePunkt(mp)
            self.render(mainscreen, self.font_menu, self.punkt)

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        sys.exit()
                    if e.key == pygame.K_UP:
                        if self.punkt > 0:
                            self.punkt -= 1
                    if e.key == pygame.K_DOWN:
                        if self.punkt < (len(self.punkts) - 1):
                            self.punkt += 1
                if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                    return self.doneWithPunkt()

            window.blit(mainscreen, (0, 0))
            window.blit(rightscreen, (720, 0))
            mainscreen.blit(self.i_menu, (0, 0))
            rightscreen.blit(self.i_rmenu, (0, 0))
            pygame.display.flip()
