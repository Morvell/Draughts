from menu import *

class PauseMenu(Menu):

    def __init__(self, punkts):
        super().__init__(punkts)

    def doneWithPunkt(self):

        continue_punkt = 0
        save = 1
        exit = 2

        if self.punkt == continue_punkt:
            return
        elif self.punkt == save:
            pass
        elif self.punkt == exit:
            sys.exit()