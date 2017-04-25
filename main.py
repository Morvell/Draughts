# -*- coding: utf-8 -*-
import endMenu
from Hahkiapi import *
from menu import *

pygame.init()

board = pygame.image.load('pic/Board.gif')
i_hb = pygame.image.load('pic/HBlack.gif')
i_hw = pygame.image.load('pic/HWhite.gif')
i_menu = pygame.image.load('pic/menu.png')

i_rightscreen = pygame.image.load('pic/rightscreen.png')



# Блок выбора цвета и стороны шашек
# side - сторона на которой будут находится белые шашки down или up


startpos(polemass, side, (i_hb, i_hw, i_db, i_dw))
done = True



punkts = [(400, 200, u'Start', (123, 15, 34), (235, 75, 156), 0),
          (400, 400, u'Exit', (123, 15, 34), (235, 75, 156), 2)]
game = Menu(punkts)
game.run()

pygame.font.init()
font = pygame.font.SysFont("monospace", 50)
fontLittle = pygame.font.SysFont("monospace", 25)

while done:

    if numberOfBlack == 0 or numberOfWhite == 0:
        endgame = endGame()
        if endgame:
            endMenu = endMenu.EndMenu()
            endMenu.run(endgame)

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
    changeNumberRender(rightscreen)
    rightscreen.blit(labalGoChess, (25, 220))
    whoGo(rightscreen)


    for i in range(10):
        for j in range(10):
            try:
                polemass[i][j].render(mainscreen)
            except(AttributeError):
                print("AttributeError check render")
            except Exception as e:
                print(e)
                print(str(i) + " " + str(j))

    pygame.display.flip()
