import pygame



class GameGUI:
    def __init__(self, gameLogic):
        pygame.init()
        pygame.font.init()

        self.logic = gameLogic

        self.board = pygame.image.load('pic/Board.gif')
        self.i_hb = pygame.image.load('pic/HBlack.gif')
        self.i_hw = pygame.image.load('pic/HWhite.gif')
        self.i_db = pygame.image.load('pic/DBlack.gif')
        self.i_dw = pygame.image.load('pic/DWhite.gif')
        self.i_menu = pygame.image.load('pic/menu.png')

        self.font = pygame.font.SysFont("monospace", 50)
        self.fontLittle = pygame.font.SysFont("monospace", 25)

        self.labelWhiteChess = self.font.render("Белые", 1, (255, 255, 255))
        self.labelBlackChess = self.font.render("Черные", 1, (0, 0, 0))
        self.labalGoChess = self.font.render("Ходят", 1, (78, 226, 14))

        self.i_rightscreen = pygame.image.load('pic/rightscreen.png')

        self.window = pygame.display.set_mode((920, 720))
        pygame.display.set_caption(u"Hahki")
        pygame.display.set_icon(pygame.image.load('pic/DBlack.gif').convert())
        self.mainscreen = pygame.Surface((720, 720))
        self.rightscreen = pygame.Surface((280, 720))

    def set_start_position(self):
        if self.logic.playerchess == "black":
            self.logic.startpos("up", (self.i_hb, self.i_hw, self.i_db, self.i_dw))
        else:
            self.logic.startpos("down", (self.i_hb, self.i_hw, self.i_db, self.i_dw))

    def changeNumberRender(self):
        """
        Отображает количество шашек на поле
        """
        labelWhite = self.font.render(str(self.logic.numberOfWhite), 1, (255, 255, 255))
        labelBlack = self.font.render(str(self.logic.numberOfBlack), 1, (0, 0, 0))
        self.rightscreen.blit(labelWhite, (70, 20))
        self.rightscreen.blit(labelBlack, (70, 120))

    def whoGoRender(self):
        """
        Отображает кто должен ходить 
        """
        if self.logic.gochess == "white":
            self.rightscreen.blit(self.labelWhiteChess, (25, 300))
        else:
            self.rightscreen.blit(self.labelBlackChess, (15, 300))

    def renderGame(self):
        for i in range(10):
            for j in range(10):
                try:
                    self.logic.polemass[i][j].render(self.mainscreen)
                except AttributeError:
                    print("AttributeError check render")
                except Exception as e:
                    print(e)
                    print(str(i) + " " + str(j))

    def render(self):
        self.window.blit(self.mainscreen, (0, 0))
        self.window.blit(self.rightscreen, (720, 0))
        self.rightscreen.blit(self.i_rightscreen, (0, 0))
        self.mainscreen.blit(self.board, (0, 0))
        self.rightscreen.blit(self.labalGoChess, (25, 220))
        self.changeNumberRender()
        self.whoGoRender()
        self.renderGame()

        pygame.display.flip()
