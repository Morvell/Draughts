# -*- coding: utf-8 -*-
import endMenu
from Hahkiapi import *
from MainMenu import *
from GameGUI import *


gameGUI = GameGUI()
mainGame = HahkiAPI()

done = True

punkts = [(300, 200, u'Simple Game', (123, 15, 34), (235, 75, 156), 0),
          (300, 300, u'Game with AI', (123, 15, 34), (235, 75, 156), 1),
          (400, 400, u'Exit', (123, 15, 34), (235, 75, 156), 2)]

game = MainMenu(punkts)
game_type, selectchess = game.run()

if game_type == "AI":
    mainGame.set_AI(True)

mainGame.set_playerchess(selectchess)


if mainGame.playerchess == "black":
    mainGame.startpos("up", (gameGUI.i_hb, gameGUI.i_hw, mainGame.i_db, mainGame.i_dw))
else:
    mainGame.startpos("down", (gameGUI.i_hb, gameGUI.i_hw, mainGame.i_db, mainGame.i_dw))

while done:

    endgame, whoWin = mainGame.endGame()
    if endgame:
        endMenu = endMenu.EndMenu()
        endMenu.run(whoWin)

    mp = pygame.mouse.get_pos()

    for e in pygame.event.get():

        if e.type == pygame.QUIT:
            done = False

        if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1 :
            mainGame.without_net(mp)

    mainGame.changeNumberRender(gameGUI.rightscreen)
    mainGame.whoGo(gameGUI.rightscreen)
    mainGame.renderGame(gameGUI.mainscreen)
    gameGUI.render()

