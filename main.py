import endMenu
from DraughtsAPI import DraughtsAPI
from GameGUI import GameGUI
from MainMenu import MainMenu
import time


def new_game(punkts):
    game = DraughtsAPI()
    gameGUI = GameGUI(game)
    mainMenu = MainMenu(punkts)
    game_type, selectchess = mainMenu.run()

    if game_type == "load":
        with open("load.txt", "r") as f:
            string = f.read()
            game.load_game(string)

    elif game_type == "AI":
        game.AI = True
        game.playerDraughts = selectchess
        gameGUI.set_start_position()
    else:
        game.playerDraughts = selectchess
        gameGUI.set_start_position()
    return game, gameGUI


punkts = [(300, 200, u'Simple Game', (123, 15, 34), (235, 75, 156), 0),
          (300, 300, u'Game with AI', (123, 15, 34), (235, 75, 156), 1),
          (400, 400, u'Load', (123, 15, 34), (235, 75, 156), 2),
          (400, 500, u'Exit', (123, 15, 34), (235, 75, 156), 3)]

game, gameGUI = new_game(punkts)

done = True

newGame = False

while done:

    time.sleep(0.05)

    if newGame:
        game, gameGUI = new_game(punkts)
        newGame = False

    endgame, gameresult = game.check_end_game()
    if endgame:
        EndMenu = endMenu.EndMenu()
        newGame = EndMenu.run(gameresult)
    else:
        gameGUI.render()

    done = gameGUI.mouse_event_check()
