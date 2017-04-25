# -*- coding: utf-8 -*-
import pygame

import Hahki

numberOfWhite = 20
numberOfBlack = 20

font = pygame.font.SysFont("monospace", 50)

last_kill = "kletka"

labelWhite = font.render(str(numberOfWhite), 1, (255, 255, 255))
labelBlack = font.render(str(numberOfBlack), 1, (0, 0, 0))

labelWhiteChess = font.render("Белые", 1, (255, 255, 255))
labalBlackChess = font.render("Черные", 1, (0, 0, 0))

side = 'down'
playerchess = 'black'
gochess = 'white'

polemass = []

mouse_button_down_fl = False
continuehod = False
continuehahka = None

ipos = 0
jpos = 0

lengthOrWidth = 72

i_db = pygame.image.load('pic/DBlack.gif')
i_dw = pygame.image.load('pic/DWhite.gif')

def whoGo(surface):
    if gochess == "white":
        surface.blit(labelWhiteChess, (25, 300))
    else:
        surface.blit(labalBlackChess, (15, 300))

def without_net(mp):
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
                        if hod_with_enemy(mass, ipos, jpos, i, j):
                            changeNumber()

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

def changeNumberRender(surface):
    surface.blit(labelWhite, (70, 20))
    surface.blit(labelBlack, (70, 120))

def changeNumber():
    global numberOfBlack, numberOfWhite
    if how_kill() == "white":
        numberOfWhite -= 1
    else:
        numberOfBlack -= 1
    global labelBlack, labelWhite
    labelWhite = font.render(str(numberOfWhite), 1, (255, 255, 255))
    labelBlack = font.render(str(numberOfBlack), 1, (0, 0, 0))
    print(str(numberOfWhite) + "|" + str(numberOfBlack))

def endGame():
    ishod = False
    if numberOfWhite == 0:
        if playerchess == "white":
            ishod = "lose"
        else:
            ishod = "win"
    elif numberOfBlack == 0:
        if playerchess == "white":
            ishod = "win"
        else:
            ishod = "lose"
    return ishod

def how_kill():
    """
    функция для распознования цвета последней сбитой шашки
    :return: цвет сбитой шишки "black" or "white"
    """
    if last_kill == "black":
        return "black"
    elif last_kill == "white":
        return "white"


def hod_with_enemy(mass, ipos, jpos, i, j):
    """
    реализует ход через врага
    :param polemass: массив данных доски
    :param mass: массив с потенциальными врагами полученный вызовом функции check_enemy
    :param ipos: 1 индекс чем ходить
    :param jpos: 2 индекс чем ходить
    :param i: 1 индекс куда пойдем
    :param j: 2 индекс куда пойдем
    :return: True если ход осуществим иначе False
    """
    for e in mass:
        if polemass[e[0]][e[1]] == polemass[i][j]:
            hod(polemass, ipos, jpos, i, j)
            kletka = Hahki.Kletka(polemass[e[2]][e[3]].x, polemass[e[2]][e[3]].y, 'kletka')
            vid = polemass[e[2]][e[3]].vid
            if vid == "white":
                global last_kill
                last_kill = "white"
            else:
                last_kill = "black"
            polemass[e[2]][e[3]] = kletka
            return True

    return False


def hod(polemass, ipos, jpos, i, j):
    """
    производит простой ход пешки
    :param polemass: массив двнных о доске
    :param ipos: начальная позиция 1
    :param jpos: начальная позиция 2
    :param i: куда ходит 1
    :param j: куда ходит 2
    :return: заполняет массив передеанный массив
    """
    dopnow = polemass[i][j].getpos()
    dopold = polemass[ipos][jpos].getpos()
    polemass[ipos][jpos].setpos(dopnow)
    polemass[i][j] = polemass[ipos][jpos]
    polemass[ipos][jpos] = Hahki.Kletka(dopold[0], dopold[1])


def checkchess(mp, polemass, i, j):
    """
    производит проверку на принадлежность указателя мыши клетке на доске
    :param mp: данные о указатели мыши
    :param polemass: массив данных л доске
    :param i: 1 индекс в массиве
    :param j: 2 индекс в массиве
    :return: True если мышь находится на i и j  позиции или False в противном
    """
    return (polemass[i][j].x < mp[0] < (polemass[i][j].x + lengthOrWidth) and polemass[i][j].y < mp[1] <
            (polemass[i][j].y + lengthOrWidth))


def check_hod_without_enemy(chess, poss):
    """
    проверяет можно ли сходить на передоваемую клетку по правилам
    :param chess: данные шашки
    :param poss: данные поля куда хочет пойти игрок
    :return: True если на это поле можно сходить или False если нет
    """

    if chess.x != poss.x - lengthOrWidth and chess.x != poss.x + lengthOrWidth:
        return False

    elif chess.side == 'down':
        if chess.y != poss.y + lengthOrWidth:
            return False
        else:
            return True
    elif chess.side == 'up':
        if chess.y != poss.y - lengthOrWidth:
            return False
        else:
            return True


def check_enemy(polemass, chess, ipos, jpos):
    """
    проверяет наличие вражеской пешки в зоне досягаемости c озможностью её срубить
    :param polemass: массив доски
    :param chess: данные о шашке которой будут ходить
    :param ipos: первый индекс chess в mass
    :param jpos: второй индекс chess в mass
    :return: массив touple со всеми возможными врагами состоящий из/
            (1 индекс в mass поля для сруба, 2 индекс в mass для для сруба, 1 индекс врага, 2 индекс врага,(ipos,jpos))
    """
    enemymass = []
    for i in (1, -1):
        for j in (1, -1):
            if ipos + i < 0 or ipos + i > 9 or jpos + j < 0 or jpos + j > 9:
                continue

            elif polemass[ipos + i][jpos + j].vid != 'kletka':
                if polemass[ipos + i][jpos + j].vid != chess.vid:
                    if ipos + 2 * i < 0 or ipos + 2 * i > 9 or jpos + 2 * j < 0 or jpos + 2 * j > 9:
                        continue
                    elif polemass[ipos + 2 * i][jpos + 2 * j].vid == 'kletka':
                        enemymass.append((ipos + 2 * i, jpos + 2 * j, ipos + i, jpos + j, (ipos, jpos)))

    return enemymass


def startpos(mass, side='down', i_mass=[]):
    """
    Задает массив доски с шашками
    :param mass: массив в который будут заносится данные
    :param side: сторона игрока down или up
    :return: ничего не возвращает тк заполняет преданный массив
    """
    i_hb = i_mass[0]
    i_hw = i_mass[1]
    for i in range(10):
        mass.append([])
        for j in range(10):
            mass[i].append([])
    if side == 'down':
        for i in (0, 2):
            for j in range(10)[1::2]:
                mass[i][j] = Hahki.Hahka(lengthOrWidth * j, lengthOrWidth * i, 'black', i_hb, 'up')
        for i in (1, 3):
            for j in range(10)[::2]:
                mass[i][j] = Hahki.Hahka(lengthOrWidth * j, lengthOrWidth * i, 'black', i_hb, 'up')
        for i in (6, 8):
            for j in range(10)[1::2]:
                mass[i][j] = Hahki.Hahka(lengthOrWidth * j, lengthOrWidth * i, 'white', i_hw, 'down')
        for i in (7, 9):
            for j in range(10)[::2]:
                mass[i][j] = Hahki.Hahka(lengthOrWidth * j, lengthOrWidth * i, 'white', i_hw, 'down')

    elif side == 'up':
        for i in (0, 2):
            for j in range(10)[1::2]:
                mass[i][j] = Hahki.Hahka(lengthOrWidth * j, lengthOrWidth * i, 'white', i_hw, 'up')
        for i in (1, 3):
            for j in range(10)[::2]:
                mass[i][j] = Hahki.Hahka(lengthOrWidth * j, lengthOrWidth * i, 'white', i_hw, 'up')
        for i in (6, 8):
            for j in range(10)[1::2]:
                mass[i][j] = Hahki.Hahka(lengthOrWidth * j, lengthOrWidth * i, 'black', i_hb, 'down')
        for i in (7, 9):
            for j in range(10)[::2]:
                mass[i][j] = Hahki.Hahka(lengthOrWidth * j, lengthOrWidth * i, 'black', i_hb, 'down')

    for i in range(10):
        for j in range(10):
            if type(mass[i][j]) == list:
                mass[i][j] = Hahki.Kletka(lengthOrWidth * j, lengthOrWidth * i)


def check_chess_with_enemy(mass, gocolor):
    """
    оставляет массив с возможными клетками которыми можно сходить срубив врага
    :param mass: массив данных доски
    :param gocolor: цвет шашек которыми будут ходить
    :return: массив результатов функции check_enemy()
    """
    arraychess = []
    for i in range(10):
        for j in range(10):
            if mass[i][j].vid == 'kletka' or mass[i][j].vid != gocolor:
                continue
            else:
                arraychess.append(check_enemy(mass, mass[i][j], i, j))
    return arraychess


def check_correct_chess(datamass, corrrectdatamass, chess):
    """
    проверяет на правельность хода если есть что рубить
    :param datamass: массив с данными доски
    :param corrrectdatamass: массив с данными шашек которые могут ходить полученный из вызова функции check_chess_with_enemy
    :param chess: шашка которой будут ходить
    :return: True если можно сходить иначе False
    """
    fl = True
    for f in corrrectdatamass:
        if len(f) == 0:
            continue
        for e in f:
            fl = False
            if datamass[e[4][0]][e[4][1]] == chess:
                return True
    return fl


def check_correct_damka_hod(chess, poss):
    """
        проверяет на правельность хода если шашка дамка
        :param chess: данные передвигаемой шашки
        :param poss: данные клетки на которую юудет поизводится движение
        :return True если можно сходить иначе False
    """
    if chess.x != poss.x - lengthOrWidth and chess.x != poss.x + lengthOrWidth:
        return False

    elif chess.side == 'down':
        if chess.y != poss.y + lengthOrWidth and chess.y != poss.y - lengthOrWidth:
            return False
    return True


def set_damka(polemass, i, j):
    """
        стонавливает шашку дамкой
        :param polemass: массив с данными доски
        :param i: первый индекс меняемой шашки в массиве polemass
        :param j: второй индекс меняемой шашки в массиве polemass
        :return: ничего
        """
    if i == 0 or i == 9:
        polemass[i][j].damka = True
        if polemass[i][j].vid == 'black':
            polemass[i][j].updatebitmap(i_db)
        else:
            polemass[i][j].updatebitmap(i_dw)
