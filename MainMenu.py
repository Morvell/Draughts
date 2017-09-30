from menu import *
from MenuSide import MenuSide


class MainMenu(Menu):
    def __init__(self, punkts):
        super().__init__(punkts)

    def done_with_punkt(self):

        easy_game = 0
        AI_game = 1
        load = 2
        exit = 3

        if self.punkt == easy_game:
            self.done = False
            menu_s = MenuSide()
            select = menu_s.run()
            self.game_type = "easy"
            self.game_side = select
            return self.game_type, self.game_side
        if self.punkt == AI_game:
            self.done = False
            menu_s = MenuSide()
            select = menu_s.run()
            self.game_type = "AI"
            self.game_side = select
            return self.game_type, self.game_side
        elif self.punkt == load:
            self.done = False
            return "load", "up"

        elif self.punkt == exit:
            sys.exit()
