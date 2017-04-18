# -*- coding: utf-8 -*-
class Kletka:
    def __init__(self, xpos, ypos, vid='kletka'):
        self.x = xpos
        self.y = ypos
        self.vid = vid

    def setpos(self, pos):
        self.x = pos[0]
        self.y = pos[1]

    def getpos(self):
        return (self.x, self.y)

    def render(self, screen):
        pass


class Hahka(Kletka):
    def __init__(self, xpos, ypos, vid, bitmap, side):
        super().__init__(xpos, ypos, vid)
        self.bitmap = bitmap
        self.bitmap.set_colorkey((255, 255, 255))
        self.side = side
        self.damka = False

    def render(self, screen):

        screen.blit(self.bitmap, (self.x, self.y))

    def updatebitmap(self,newbitmap):
        self.bitmap = newbitmap
        self.bitmap.set_colorkey((255, 255, 255))


