from menu import *


class PauseMenu(Menu):
    def __init__(self, punkts, func=None):
        super().__init__(punkts)
        self.func = func

    def done_with_punkt(self):

        continue_punkt = 0
        save = 1
        exit = 2

        if self.punkt == continue_punkt:
            return
        elif self.punkt == save:
            with open("load.txt", "w") as f:
                f.write(self.func())

        elif self.punkt == exit:
            sys.exit()
