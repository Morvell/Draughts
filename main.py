# -*- coding: utf-8 -*-
import endMenu
from Hahkiapi import *
from MainMenu import *
from GameGUI import *

game = HahkiAPI()
gameGUI = GameGUI(game)

done = True

punkts = [(300, 200, u'Simple Game', (123, 15, 34), (235, 75, 156), 0),
          (300, 300, u'Game with AI', (123, 15, 34), (235, 75, 156), 1),
          (400, 400, u'Exit', (123, 15, 34), (235, 75, 156), 2)]

mainMenu = MainMenu(punkts)
game_type, selectchess = mainMenu.run()

if game_type == "AI":
    game.set_AI(True)

game.set_playerchess(selectchess)

gameGUI.set_start_position()

while done:

    endgame, whoWin = game.endGame()
    if endgame:
        endMenu = endMenu.EndMenu()
        endMenu.run(whoWin)

    mp = pygame.mouse.get_pos()

    for e in pygame.event.get():

        if e.type == pygame.QUIT:
            done = False

        if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1 :
            game.without_net(mp)

    game.whoGo(gameGUI.rightscreen)
    game.renderGame(gameGUI.mainscreen)
    gameGUI.render()

