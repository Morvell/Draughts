import endMenu
from Hahkiapi import HahkiAPI
from MainMenu import MainMenu
from GameGUI import GameGUI


def new_game(punkts):
    game = HahkiAPI()
    gameGUI = GameGUI(game)
    mainMenu = MainMenu(punkts)
    game_type, selectchess = mainMenu.run()

    if game_type == "AI":
        game.AI = True

    game.playerDraughts = selectchess

    gameGUI.set_start_position()
    return game, gameGUI


punkts = [(300, 200, u'Simple Game', (123, 15, 34), (235, 75, 156), 0),
          (300, 300, u'Game with AI', (123, 15, 34), (235, 75, 156), 1),
          (400, 400, u'Exit', (123, 15, 34), (235, 75, 156), 2)]

game, gameGUI = new_game(punkts)

done = True

newGame = False

while done:

    if newGame:
        game, gameGUI = new_game(punkts)
        newGame = False

    endgame, gameresult = game.check_end_game()
    print(str(endgame) + " " + str(gameresult))
    if endgame:
        EndMenu = endMenu.EndMenu()
        newGame = EndMenu.run(gameresult)
    else:
        gameGUI.render()

    done = gameGUI.mouseEventCheck()
