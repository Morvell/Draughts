# -*- coding: utf-8 -*-
import endMenu
from Hahkiapi import *
from MainMenu import *

pygame.init()

board = pygame.image.load('pic/Board.gif')
i_hb = pygame.image.load('pic/HBlack.gif')
i_hw = pygame.image.load('pic/HWhite.gif')
i_menu = pygame.image.load('pic/menu.png')

i_rightscreen = pygame.image.load('pic/rightscreen.png')

window = pygame.display.set_mode((920, 720))
pygame.display.set_caption(u"Hahki")
pygame.display.set_icon(pygame.image.load('pic/DBlack.gif').convert())
mainscreen = pygame.Surface((720, 720))
rightscreen = pygame.Surface((280, 720))


done = True

punkts = [(300, 200, u'Simple Game', (123, 15, 34), (235, 75, 156), 0),
          (300, 300, u'Game with AI', (123, 15, 34), (235, 75, 156), 1),
          (400, 400, u'Exit', (123, 15, 34), (235, 75, 156), 2)]

game = MainMenu(punkts)
game_type, game_AI, selectchess = game.run()
set_playerchess(selectchess)
startpos(polemass, side, (i_hb, i_hw, i_db, i_dw))

pygame.font.init()
font = pygame.font.SysFont("monospace", 50)
fontLittle = pygame.font.SysFont("monospace", 25)

while done:

    endgame, ishod = endGame()
    if endgame:
        endMenu = endMenu.EndMenu()
        endMenu.run(ishod)

    mp = pygame.mouse.get_pos()

    for e in pygame.event.get():

        if e.type == pygame.QUIT:
            done = False

        if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
            without_net(mp)

    # render text

    labalGoChess = font.render("Ходят", 1, (78, 226, 14))

    window.blit(mainscreen, (0, 0))
    window.blit(rightscreen, (720, 0))
    rightscreen.blit(i_rightscreen, (0, 0))
    mainscreen.blit(board, (0, 0))
    rightscreen.blit(labalGoChess, (25, 220))
    changeNumberRender(rightscreen)
    whoGo(rightscreen)

    renderGame(mainscreen)



    pygame.display.flip()
