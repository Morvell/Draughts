# -*- coding: utf-8 -*-
from Hahkiapi import *
from menu import *

pygame.init()

def without_net():
    global continuehod
    global continuehahka
    global mouse_button_down_fl
    global gochess
    global ipos
    global jpos
    for i in range(10):
        for j in range(10):
            if checkchess(mp, polemass, i, j):
                if continuehod == True and polemass[i][j] == continuehahka:
                    print('in False')
                    mouse_button_down_fl = True
                    continuehod = False
                    ipos = i
                    jpos = j
                elif continuehod == True and polemass[i][j] != continuehahka:
                    break
                # блок выбора шашки
                elif (mouse_button_down_fl == False or polemass[i][j].vid == gochess) and polemass[i][
                    j].vid != 'kletka' and polemass[i][j].vid == gochess:
                    if len(check_chess_with_enemy(polemass, gochess)) != 0:
                        if check_correct_chess(polemass, check_chess_with_enemy(polemass, gochess), polemass[i][j]):

                            print('in False')
                            mouse_button_down_fl = True
                            ipos = i
                            jpos = j
                            break
                        else:
                            break
                    else:
                        print('in False')
                        mouse_button_down_fl = True

                        ipos = i
                        jpos = j
                        break
                # блок хода
                elif mouse_button_down_fl == True and gochess != polemass[i][j].vid:
                    mass = check_enemy(polemass, polemass[ipos][jpos], ipos, jpos)
                    if len(mass) != 0:
                        if hod_with_enemy(polemass, mass, ipos, jpos, i, j):

                            mouse_button_down_fl = False
                            set_damka(polemass, i, j)

                            if len(check_enemy(polemass, polemass[i][j], i, j)) == 0:
                                set_damka(polemass, i, j)
                                if gochess == 'white':
                                    gochess = 'black'
                                else:
                                    gochess = 'white'
                            else:
                                set_damka(polemass, i, j)
                                continuehod = True
                                continuehahka = polemass[i][j]
                            break


                    elif (check_hod_without_enemy(polemass[ipos][jpos], polemass[i][j]) or (
                                polemass[ipos][jpos].damka and check_correct_damka_hod(polemass[ipos][jpos],
                                                                                       polemass[i][j]))) and \
                                    polemass[i][
                                        j].vid == 'kletka':
                        print('in True')
                        mouse_button_down_fl = False
                        hod(polemass, ipos, jpos, i, j)
                        set_damka(polemass, i, j)
                        if gochess == 'white':
                            gochess = 'black'
                        else:
                            gochess = 'white'
                        break


board = pygame.image.load('pic\Board.gif')
i_hb = pygame.image.load('pic\HBlack.gif')
i_hw = pygame.image.load('pic\HWhite.gif')

i_rightscreen = pygame.image.load('pic\\rightscreen.png')

polemass = []

# Блок выбора цвета и стороны шашек
# side - сторона на которой будут находится белые шашки down или up
side = 'down'
playerchess = 'black'
gochess = 'white'

startpos(polemass, side, (i_hb, i_hw, i_db, i_dw))
done = True

mouse_button_down_fl = False
continuehod = False
continuehahka = None

ipos = 0
jpos = 0

punkts = [(400, 200, u'Start', (123, 15, 34), (235, 75, 156), 0),
          (400, 400, u'Exit', (123, 15, 34), (235, 75, 156), 2)]
game = Menu(punkts)
game.run()

while done:
    mp = pygame.mouse.get_pos()

    for e in pygame.event.get():

        if e.type == pygame.QUIT:
            done = False
        if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
            without_net()

    font = pygame.font.SysFont("monospace", 50)

    # render text
    labelWhite = font.render("20", 1, (255, 255, 255))
    labelBlack = font.render("20", 1, (0, 0, 0))


    window.blit(mainscreen, (0, 0))
    window.blit(rightscreen, (720, 0))
    rightscreen.blit(i_rightscreen, (0, 0))
    rightscreen.blit(labelWhite, (70, 30))
    rightscreen.blit(labelBlack, (70, 120))
    mainscreen.blit(board, (0, 0))

    for i in range(10):
        for j in range(10):
            try:
                polemass[i][j].render(mainscreen)
            except(AttributeError):
                print("AttributeError check render")
            except Exception as e:
                print(e)
                # print(str(i) + " " + str(j))

    pygame.display.flip()
