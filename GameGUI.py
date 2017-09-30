import pygame
from PauseMenu import PauseMenu


class GameGUI:
    def __init__(self, gameLogic):
        pygame.font.init()

        self.lengthOrWidth = 72

        self.logic = gameLogic

        self.board = pygame.image.load('pic/Board.gif')
        self.i_hb = pygame.image.load('pic/HBlack.gif')
        self.i_hw = pygame.image.load('pic/HWhite.gif')
        self.i_db = pygame.image.load('pic/DBlack.gif')
        self.i_dw = pygame.image.load('pic/DWhite.gif')
        self.i_menu = pygame.image.load('pic/menu.png')

        self.i_hb.set_colorkey((255, 255, 255))
        self.i_hw.set_colorkey((255, 255, 255))
        self.i_db.set_colorkey((255, 255, 255))
        self.i_dw.set_colorkey((255, 255, 255))

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

    def mouseEventCheck(self):
        """
        обрабатывает движение мыши
        :return: True или False если пользователь закрыл игру
        """
        mp = pygame.mouse.get_pos()
        done = True

        for e in pygame.event.get():

            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    punkts = [(365, 200, u'Continue', (123, 15, 34), (235, 75, 156), 0),
                              (400, 300, u'Save', (123, 15, 34), (235, 75, 156), 1),
                              (400, 400, u'Exit', (123, 15, 34), (235, 75, 156), 2)]
                    pause = PauseMenu(punkts, self.logic.save_game)
                    pause.run()

            if e.type == pygame.QUIT:
                done = False

            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                self.logic.without_net(mp)

        return done

    def set_start_position(self):
        """
        устонавливет сартовую позицию
        """
        if self.logic.playerDraughts == "b":
            self.logic.set_start_playing_field("up")
        else:
            self.logic.set_start_playing_field("down")

    def changeNumberRender(self):
        """
        Отображает количество шашек на поле
        """
        labelWhite = self.font.render(str(self.logic.numberOfWhite), 1, (255, 255, 255))
        labelBlack = self.font.render(str(self.logic.numberOfBlack), 1, (0, 0, 0))
        self.rightscreen.blit(labelWhite, (70, 20))
        self.rightscreen.blit(labelBlack, (70, 120))

    def step_history(self):
        n = len(self.logic.stepArray)
        for i in range(n):
            if self.logic.stepArray.get_color(i) == 'b':
                labelOne = self.fontLittle.render(str(self.logic.stepArray.get_first(i)), 1, (0, 0, 0))
                labelTwo = self.fontLittle.render(str(self.logic.stepArray.get_second(i)), 1, (0, 0, 0))
            else:
                labelOne = self.fontLittle.render(str(self.logic.stepArray.get_first(i)), 1, (188, 22, 22))
                labelTwo = self.fontLittle.render(str(self.logic.stepArray.get_second(i)), 1, (188, 22, 22))

            self.rightscreen.blit(labelOne, (5, 370 + (n - i) * 35))
            self.rightscreen.blit(labelTwo, (100, 370 + (n - i) * 35))

    def whoGoRender(self):
        """
        Отображает кто должен ходить 
        """
        if self.logic.playDraughts == "w":
            self.rightscreen.blit(self.labelWhiteChess, (25, 300))
        else:
            self.rightscreen.blit(self.labelBlackChess, (15, 300))

    def renderGameField(self):
        """
        отрисовывает игровое поле 
        """
        for i in range(10):
            for j in range(10):
                try:
                    if self.logic.gameField[i][j] == 'b':
                        self.mainscreen.blit(self.i_hb, (j * self.lengthOrWidth, i * self.lengthOrWidth))
                    elif self.logic.gameField[i][j] == 'w':
                        self.mainscreen.blit(self.i_hw, (j * self.lengthOrWidth, i * self.lengthOrWidth))

                    elif self.logic.gameField[i][j] == 'q':
                        self.mainscreen.blit(self.i_dw, (j * self.lengthOrWidth, i * self.lengthOrWidth))
                    elif self.logic.gameField[i][j] == 'v':
                        self.mainscreen.blit(self.i_db, (j * self.lengthOrWidth, i * self.lengthOrWidth))

                    self.logic.gameField[i][j].render(self.mainscreen)
                except AttributeError:
                    None
                except Exception as e:
                    print(e)
                    print(str(i) + " " + str(j))

    def render(self):
        """
        отрисовка всего
        """
        self.window.blit(self.mainscreen, (0, 0))
        self.window.blit(self.rightscreen, (720, 0))
        self.rightscreen.blit(self.i_rightscreen, (0, 0))
        self.mainscreen.blit(self.board, (0, 0))
        self.rightscreen.blit(self.labalGoChess, (25, 220))
        self.changeNumberRender()
        self.whoGoRender()
        self.step_history()
        self.renderGameField()

        pygame.display.flip()
