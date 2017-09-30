from menu import *


class MenuSide(Menu):


    def __init__(self, punkts = [(380, 200, u'White', (123, 15, 34), (235, 75, 156), 0),
                       (390, 300, u'Black', (123, 15, 34), (235, 75, 156), 1),
                       (400, 400, u'Exit', (123, 15, 34), (235, 75, 156), 2)]):
        super().__init__(punkts)

    def done_with_punkt(self):
        white = 0
        black = 1
        exit = 2
        if self.punkt == white:
            self.done = False
            return "w"

        if self.punkt == black:
            self.done = False
            return "b"

        elif self.punkt == exit:
            sys.exit()

