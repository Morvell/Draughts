from menu import *
from MenuSide import MenuSide


class MainMenu(Menu):

    def __init__(self, punkts):
        super().__init__(punkts)

    def doneWithPunkt(self):

        easy_game = 0
        AI_game = 1
        exit = 2

        if self.punkt == easy_game:
            self.done = False
            menuS = MenuSide()
            select = menuS.run()
            self.game_type = "easy"
            self.game_side = select
            return self.game_type, self.game_side
        if self.punkt == AI_game:
            self.done = False
            menuS = MenuSide()
            select = menuS.run()
            self.game_type = "AI"
            self.game_side = select
            return self.game_type, self.game_side

        elif self.punkt == exit:
            sys.exit()