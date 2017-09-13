import pygame
import sys

window = pygame.display.set_mode((920, 720))
pygame.display.set_caption(u"Hahki")
pygame.display.set_icon(pygame.image.load('pic/DBlack.gif').convert())
mainscreen = pygame.Surface((720, 720))
rightscreen = pygame.Surface((280, 720))

pygame.font.init()
font = pygame.font.SysFont("monospace", 50)

labalWin = font.render("Победа", 1, (255, 0, 0))
labelLose = font.render("Проигрышь", 1, (0, 0, 0))


class EndMenu:
    def __init__(self):
        self.punkts = [
                  (390, 300, u'Restart', (123, 15, 34), (235, 75, 156), 0),
                  (400, 400, u'Exit', (123, 15, 34), (235, 75, 156), 1)]
        self.i_menu = pygame.image.load('pic/menu.png')
        self.i_rmenu = pygame.image.load('pic/menurightscreen.png')
        self.punkt = 0

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
        restart = 0
        exit = 1

        if self.punkt == restart:
            self.done = False
            return "restart"

        elif self.punkt == exit:
            sys.exit()
       

    def run(self, ishod):
        done = True

        label = labalWin
        if ishod == "lose":
            label = labelLose

        while done:
            self.render(mainscreen,font,self.punkt)


            mp = pygame.mouse.get_pos()
            self.collaidePunkt(mp)

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
                if (e.type == pygame.MOUSEBUTTONDOWN and e.button == 1) or (
                        e.type == pygame.KEYDOWN and e.key == pygame.K_RIGHT):
                    return self.doneWithPunkt()


            window.blit(mainscreen, (0, 0))
            window.blit(rightscreen, (720, 0))
            mainscreen.blit(self.i_menu, (0, 0))
            mainscreen.blit(label, (380, 200))
            rightscreen.blit(self.i_rmenu, (0, 0))
            pygame.display.flip()
