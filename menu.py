import pygame
import sys

window = pygame.display.set_mode((920, 720))
pygame.display.set_caption(u"Hahki")
pygame.display.set_icon(pygame.image.load('pic/DBlack.gif').convert())
mainscreen = pygame.Surface((720, 720))
rightscreen = pygame.Surface((280, 720))


class Menu:
    def __init__(self, punkts=(300, 300, u'start', (123, 235, 34), (34, 25, 66), 1)):
        super().__init__()
        self.i_menu = pygame.image.load('pic/menu.png')
        self.i_rmenu = pygame.image.load('pic/menurightscreen.png')
        self.punkts = punkts

    def render(self, poverhnost, font, num_punkt):
        for e in self.punkts:
            if num_punkt == e[5]:
                poverhnost.blit(font.render(e[2], 1, e[4]), (e[0], e[1]))
            else:
                poverhnost.blit(font.render(e[2], 1, e[3]), (e[0], e[1]))

    def run(self):
        done = True
        font_menu = pygame.font.SysFont("comicsansms", 50)
        punkt = 0
        while done:

            mp = pygame.mouse.get_pos()

            for i in self.punkts:
                if mp[0] > i[0] and mp[0] < (i[0] + 155) and mp[1] > i[1] and mp[1] < (i[1] + 50):
                    punkt = i[5]
            self.render(mainscreen, font_menu, punkt)
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        sys.exit()
                    if e.key == pygame.K_UP:
                        if punkt > 0:
                            punkt -= 1
                    if e.key == pygame.K_DOWN:
                        if punkt < (len(self.punkts) - 1):
                            punkt += 1
                if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                    if punkt == 0:
                        done = False

                    elif punkt == 2:
                        sys.exit()

            window.blit(mainscreen, (0, 0))
            window.blit(rightscreen, (720, 0))
            mainscreen.blit(self.i_menu, (0, 0))
            rightscreen.blit(self.i_rmenu, (0, 0))
            pygame.display.flip()
