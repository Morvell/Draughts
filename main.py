import endMenu
from Hahkiapi import HahkiAPI
from MainMenu import MainMenu
from GameGUI import GameGUI

game = HahkiAPI()
gameGUI = GameGUI(game)

punkts = [(300, 200, u'Simple Game', (123, 15, 34), (235, 75, 156), 0),
          (300, 300, u'Game with AI', (123, 15, 34), (235, 75, 156), 1),
          (400, 400, u'Exit', (123, 15, 34), (235, 75, 156), 2)]

mainMenu = MainMenu(punkts)
game_type, selectchess = mainMenu.run()

if game_type == "AI":
    game.AI = True

game.playerDraught = selectchess

gameGUI.set_start_position()

done = True

while done:

    endgame, gameresult = game.check_end_game()
    if endgame:
        endMenu = endMenu.EndMenu()
        endMenu.run(gameresult)

    done = gameGUI.mouseEventCheck()

    gameGUI.render()

