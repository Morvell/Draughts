# -*- coding: utf-8 -*-
import Hahki


class HahkiAPI:
    def __init__(self):
        self.numberOfWhite = 20
        self.numberOfBlack = 20

        self.last_kill = "kletka"

        self.side = 'down'
        self.playerchess = 'black'
        self.gochess = 'white'
        self.AI = False

        self.polemass = []

        self.mouse_button_down_fl = False
        self.continuehod = False
        self.continuehahka = None

        self.ipos = 0
        self.jpos = 0

        self.lengthOrWidth = 72

    def set_AI(self, select):
        self.AI = select

    def set_playerchess(self, select):
        self.playerchess = select



    def without_net(self, mp):
        """
        Основная логика программы
        :param mp: координаты мышки
        """

        if self.AI and self.gochess != self.playerchess:
            for i in range(10):
                for j in range(10):
                    self.gameLogic(i, j)
        else:
            i, j = self.checkchess(mp)
            self.gameLogic(i, j)


    def gameLogic(self, i, j):

        if self.continuehod and self.polemass[i][j] == self.continuehahka:
            print("#1")
            self.mouse_button_down_fl = True
            self.continuehod = False
            self.ipos = i
            self.jpos = j
        elif self.continuehod and self.polemass[i][j] != self.continuehahka:
            print("#2")
            return
            # блок выбора шашки
        elif (self.mouse_button_down_fl == False or self.polemass[i][j].vid == self.gochess) and self.polemass[i][
            j].vid != 'kletka' and self.polemass[i][j].vid == self.gochess:
            print("#3")
            if len(self.check_chess_with_enemy(self.gochess)) != 0:
                print("#4")
                if self.check_correct_chess(self.check_chess_with_enemy(self.gochess), self.polemass[i][j]):
                    print("#5")
                    self.mouse_button_down_fl = True
                    self.ipos = i
                    self.jpos = j
                return
            else:
                print("#6")
                self.mouse_button_down_fl = True
                self.ipos = i
                self.jpos = j
                return
                # блок хода
        elif self.mouse_button_down_fl and self.gochess != self.polemass[i][j].vid:
            print("#7")
            massWithEnemy = self.check_enemy(self.polemass[self.ipos][self.jpos], self.ipos, self.jpos)
            if len(massWithEnemy) != 0:
                print("#8")
                if self.hod_with_enemy(massWithEnemy, self.ipos, self.jpos, i, j):
                    print("#9")
                    self.changeNumber()
                    self.mouse_button_down_fl = False
                    self.set_damka(i, j)

                    if len(self.check_enemy(self.polemass[i][j], i, j)) == 0:
                        print("#10")
                        self.set_damka(i, j)
                        if self.gochess == 'white':
                            self.gochess = 'black'
                        else:
                            self.gochess = 'white'
                    else:
                        print("#11")
                        self.set_damka(i, j)
                        self.continuehod = True
                        self.continuehahka = self.polemass[i][j]
                    return


            elif (self.check_hod_without_enemy(self.polemass[self.ipos][self.jpos], self.polemass[i][j]) or (
                        self.polemass[self.ipos][self.jpos].damka and self.check_correct_damka_hod(self.polemass[self.ipos][self.jpos],
                                                                               self.polemass[i][j]))) and \
                            self.polemass[i][j].vid == 'kletka':
                print('#12')
                self.mouse_button_down_fl = False
                self.hod(self.ipos, self.jpos, i, j)
                self.set_damka(i, j)
                if self.gochess == 'white':
                    self.gochess = 'black'
                else:
                    self.gochess = 'white'
                return





    def changeNumber(self):
        """
        Изменяет количество шашек на игровом столе
        """
        print(self.playerchess)
        if self.how_kill() == "white":
            self.numberOfWhite -= 1
        else:
            self.numberOfBlack -= 1
        print(str(self.numberOfWhite) + "|" + str(self.numberOfBlack))


    def endGame(self):
        """
        Проверка на конец игры
        :return: Tupel 
        """
        ishod = False
        endgame = False
        if self.numberOfBlack == 0 or self.numberOfWhite == 0:
            if self.numberOfWhite == 0:
                if self.playerchess == "white":
                    ishod = "lose"
                else:
                    ishod = "win"
            elif self.numberOfBlack == 0:
                if self.playerchess == "white":
                    ishod = "win"
                else:
                    ishod = "lose"
        return endgame, ishod





    def how_kill(self):
        """
        функция для распознования цвета последней сбитой шашки
        :return: цвет сбитой шишки "black" or "white"
        """
        if self.last_kill == "black":
            return "black"
        elif self.last_kill == "white":
            return "white"


    def hod_with_enemy(self, mass, ipos, jpos, i, j):
        """
        реализует ход через врага
        :param mass: массив с потенциальными врагами полученный вызовом функции check_enemy
        :param ipos: 1 индекс чем ходить
        :param jpos: 2 индекс чем ходить
        :param i: 1 индекс куда пойдем
        :param j: 2 индекс куда пойдем
        :return: True если ход осуществим иначе False
        """
        for e in mass:
            if self.polemass[e[0]][e[1]] == self.polemass[i][j]:
                self.hod(ipos, jpos, i, j)
                kletka = Hahki.Kletka(self.polemass[e[2]][e[3]].x, self.polemass[e[2]][e[3]].y, 'kletka')
                vid = self.polemass[e[2]][e[3]].vid
                if vid == "white":
                    self.last_kill = "white"
                else:
                    self.last_kill = "black"
                self.polemass[e[2]][e[3]] = kletka
                return True

        return False


    def hod(self, ipos, jpos, i, j):
        """
        производит простой ход пешки
        :param ipos: начальная позиция 1
        :param jpos: начальная позиция 2
        :param i: куда ходит 1
        :param j: куда ходит 2
        :return: заполняет массив передеанный массив
        """
        dopnow = self.polemass[i][j].getpos()
        dopold = self.polemass[ipos][jpos].getpos()
        self.polemass[ipos][jpos].setpos(dopnow)
        self.polemass[i][j] = self.polemass[ipos][jpos]
        self.polemass[ipos][jpos] = Hahki.Kletka(dopold[0], dopold[1])


    def checkchess(self, mp):
        """
        производит проверку на принадлежность указателя мыши клетке на доске
        :param mp: данные о указатели мыши
        :param i: 1 индекс в массиве
        :param j: 2 индекс в массиве
        :return: True если мышь находится на i и j  позиции или False в противном
        """
        for i in range(10):
            for j in range(10):
                if (self.polemass[i][j].x < mp[0] < (self.polemass[i][j].x + self.lengthOrWidth) and self.polemass[i][j].y < mp[1] <
                    (self.polemass[i][j].y + self.lengthOrWidth)):
                    return i, j


    def check_hod_without_enemy(self, chess, poss):
        """
        проверяет можно ли сходить на передоваемую клетку по правилам
        :param chess: данные шашки
        :param poss: данные поля куда хочет пойти игрок
        :return: True если на это поле можно сходить или False если нет
        """

        if chess.x != poss.x - self.lengthOrWidth and chess.x != poss.x + self.lengthOrWidth:
            return False

        elif chess.side == 'down':
            if chess.y != poss.y + self.lengthOrWidth:
                return False
            else:
                return True
        elif chess.side == 'up':
            if chess.y != poss.y - self.lengthOrWidth:
                return False
            else:
                return True


    def check_enemy(self, chess, ipos, jpos):
        """
        проверяет наличие вражеской пешки в зоне досягаемости c озможностью её срубить
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

                elif self.polemass[ipos + i][jpos + j].vid != 'kletka':
                    if self.polemass[ipos + i][jpos + j].vid != chess.vid:
                        if ipos + 2 * i < 0 or ipos + 2 * i > 9 or jpos + 2 * j < 0 or jpos + 2 * j > 9:
                            continue
                        elif self.polemass[ipos + 2 * i][jpos + 2 * j].vid == 'kletka':
                            enemymass.append((ipos + 2 * i, jpos + 2 * j, ipos + i, jpos + j, (ipos, jpos)))

        return enemymass


    def startpos(self, side='down', i_mass=[]):
        """
        Задает массив доски с шашками
        :param side: сторона игрока down или up
        :return: ничего не возвращает тк заполняет преданный массив
        """
        i_hb = i_mass[0]
        i_hw = i_mass[1]
        for i in range(10):
            self.polemass.append([])
            for j in range(10):
                self.polemass[i].append([])
        if side == 'down':
            for i in (0, 2):
                for j in range(10)[1::2]:
                    self.polemass[i][j] = Hahki.Hahka(self.lengthOrWidth * j, self.lengthOrWidth * i, 'black', i_hb, 'up')
            for i in (1, 3):
                for j in range(10)[::2]:
                    self.polemass[i][j] = Hahki.Hahka(self.lengthOrWidth * j, self.lengthOrWidth * i, 'black', i_hb, 'up')
            for i in (6, 8):
                for j in range(10)[1::2]:
                    self.polemass[i][j] = Hahki.Hahka(self.lengthOrWidth * j, self.lengthOrWidth * i, 'white', i_hw, 'down')
            for i in (7, 9):
                for j in range(10)[::2]:
                    self.polemass[i][j] = Hahki.Hahka(self.lengthOrWidth * j, self.lengthOrWidth * i, 'white', i_hw, 'down')

        elif side == 'up':
            for i in (0, 2):
                for j in range(10)[1::2]:
                    self.polemass[i][j] = Hahki.Hahka(self.lengthOrWidth * j, self.lengthOrWidth * i, 'white', i_hw, 'up')
            for i in (1, 3):
                for j in range(10)[::2]:
                    self.polemass[i][j] = Hahki.Hahka(self.lengthOrWidth * j, self.lengthOrWidth * i, 'white', i_hw, 'up')
            for i in (6, 8):
                for j in range(10)[1::2]:
                    self.polemass[i][j] = Hahki.Hahka(self.lengthOrWidth * j, self.lengthOrWidth * i, 'black', i_hb, 'down')
            for i in (7, 9):
                for j in range(10)[::2]:
                    self.polemass[i][j] = Hahki.Hahka(self.lengthOrWidth * j, self.lengthOrWidth * i, 'black', i_hb, 'down')

        for i in range(10):
            for j in range(10):
                if type(self.polemass[i][j]) == list:
                    self.polemass[i][j] = Hahki.Kletka(self.lengthOrWidth * j, self.lengthOrWidth * i)


    def check_chess_with_enemy(self, gocolor):
        """
        оставляет массив с возможными клетками которыми можно сходить срубив врага
        :param gocolor: цвет шашек которыми будут ходить
        :return: массив результатов функции check_enemy()
        """
        arraychess = []
        for i in range(10):
            for j in range(10):
                if self.polemass[i][j].vid == 'kletka' or self.polemass[i][j].vid != gocolor:
                    continue
                else:
                    arraychess.append(self.check_enemy(self.polemass[i][j], i, j))
        return arraychess


    def check_correct_chess(self, corrrectdatamass, chess):
        """
        проверяет на правельность хода если есть что рубить
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
                if self.polemass[e[4][0]][e[4][1]] == chess:
                    return True
        return fl


    def check_correct_damka_hod(self, chess, poss):
        """
            проверяет на правельность хода если шашка дамка
            :param chess: данные передвигаемой шашки
            :param poss: данные клетки на которую юудет поизводится движение
            :return True если можно сходить иначе False
        """
        if chess.x != poss.x - self.lengthOrWidth and chess.x != poss.x + self.lengthOrWidth:
            return False

        elif chess.side == 'down':
            if chess.y != poss.y + self.lengthOrWidth and chess.y != poss.y - self.lengthOrWidth:
                return False
        return True


    def set_damka(self, i, j):
        """
            устонавливает шашку дамкой
            :param i: первый индекс меняемой шашки в массиве polemass
            :param j: второй индекс меняемой шашки в массиве polemass
            :return: ничего
            """
        if i == 0 or i == 9:
            self.polemass[i][j].damka = True
            if self.polemass[i][j].vid == 'black':
                self.polemass[i][j].updatebitmap(self.i_db)
            else:
                self.polemass[i][j].updatebitmap(self.i_dw)
