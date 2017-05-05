import pygame



class GameGUI:
    def __init__(self, gameLogic):
        pygame.init()
        pygame.font.init()

        self.logic = gameLogic

        self.board = pygame.image.load('pic/Board.gif')
        self.i_hb = pygame.image.load('pic/HBlack.gif')
        self.i_hw = pygame.image.load('pic/HWhite.gif')
        self.i_menu = pygame.image.load('pic/menu.png')

        self.font = pygame.font.SysFont("monospace", 50)
        self.fontLittle = pygame.font.SysFont("monospace", 25)



        self.labalGoChess = self.font.render("Ходят", 1, (78, 226, 14))

        self.i_rightscreen = pygame.image.load('pic/rightscreen.png')

        self.window = pygame.display.set_mode((920, 720))
        pygame.display.set_caption(u"Hahki")
        pygame.display.set_icon(pygame.image.load('pic/DBlack.gif').convert())
        self.mainscreen = pygame.Surface((720, 720))
        self.rightscreen = pygame.Surface((280, 720))

    def set_start_position(self):
        if self.logic.playerchess == "black":
            self.logic.startpos("up", (self.i_hb, self.i_hw, self.logic.i_db, self.logic.i_dw))
        else:
            self.logic.startpos("down", (self.i_hb, self.i_hw, self.logic.i_db, self.logic.i_dw))

    def changeNumberRender(self):
        """
        Отображает количество шшашек на поле
        :param surface: поверхность для отображения
        """
        labelWhite = self.font.render(str(self.logic.numberOfWhite), 1, (255, 255, 255))
        labelBlack = self.font.render(str(self.logic.numberOfBlack), 1, (0, 0, 0))
        self.rightscreen.blit(labelWhite, (70, 20))
        self.rightscreen.blit(labelBlack, (70, 120))

    def render(self):
        self.window.blit(self.mainscreen, (0, 0))
        self.window.blit(self.rightscreen, (720, 0))
        self.rightscreen.blit(self.i_rightscreen, (0, 0))
        self.mainscreen.blit(self.board, (0, 0))
        self.rightscreen.blit(self.labalGoChess, (25, 220))
        self.changeNumberRender()

        pygame.display.flip()
