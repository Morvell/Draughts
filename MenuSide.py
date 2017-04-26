from menu import *


class MenuSide:
    done = True
    font_menu = pygame.font.SysFont("comicsansms", 50)
    punkt = 0

    def __init__(self):

        self.window = pygame.display.set_mode((920, 720))
        pygame.display.set_caption(u"Hahki")
        pygame.display.set_icon(pygame.image.load('pic/DBlack.gif').convert())
        self.mainscreen = pygame.Surface((720, 720))
        self.rightscreen = pygame.Surface((280, 720))

        self.i_menu = pygame.image.load('pic/menu.png')
        self.i_rmenu = pygame.image.load('pic/menurightscreen.png')
        self.punkts = [(380, 200, u'White', (123, 15, 34), (235, 75, 156), 0),
                       (390, 300, u'Black', (123, 15, 34), (235, 75, 156), 1),
                       (400, 400, u'Exit', (123, 15, 34), (235, 75, 156), 2)]

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
        white = 0
        black = 1
        exit = 2
        if self.punkt == white:
            self.done = False
            return "white"

        if self.punkt == black:
            self.done = False
            return "black"

        elif self.punkt == exit:
            sys.exit()

    def run(self):

        while self.done:

            mp = pygame.mouse.get_pos()
            self.collaidePunkt(mp)
            self.render(self.mainscreen, self.font_menu, self.punkt)

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
                    result = self.doneWithPunkt()
                    return result

            self.window.blit(self.mainscreen, (0, 0))
            self.window.blit(self.rightscreen, (720, 0))
            self.mainscreen.blit(self.i_menu, (0, 0))
            self.rightscreen.blit(self.i_rmenu, (0, 0))
            pygame.display.flip()
