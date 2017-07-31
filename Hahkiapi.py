class HahkiAPI:
    def __init__(self):
        self.numberOfWhite = 20
        self.numberOfBlack = 20

        self.last_kill = "kletka"

        self.side = 'up'
        self.playerchess = 'b'
        self.gochess = 'w'
        self.AI = False

        self.polemass = []

        self.mouse_button_down_fl = False
        self.continuehod = False
        self.continuehahka = None

        # ipos, jpos = позиция шашки на которую иначально выбрали для действий с ней
        self.ipos = 0
        self.jpos = 0

        self.lengthOrWidth = 72

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
        # проверка что бы не ходил на пустую клетку
        if self.polemass[i][j] == ' ':
            return

        chessWithEnemy = self.checkChessWithEnemy()
        if len(chessWithEnemy) != 0:
            if (i, j) in chessWithEnemy:
                self.ipos = i
                self.jpos = j
                self.continuehod = True
                return

            if self.continuehod and (self.polemass[self.ipos][self.jpos] == 'q' or self.polemass[self.ipos][self.jpos] == 'v') and self.accesHodForDamka(i,j):
                self.hodWithEnemyForDamka(i, j)
                if len(self.checkChessWithEnemy()) == 0:
                    self.changeGoChess()
                    self.continuehod = False
                    return
                else:
                    return

            if self.continuehod and (i, j) in self.accessHodWithEnemy(i,j):
                self.hodWithEnemy(i, j)
                if i == 0 or i == 9:
                    if self.damkaCheckAfterEnemy(i, j):
                        self.setDamka(i, j)
                if len(self.checkChessWithEnemy()) == 0:
                    self.changeGoChess()
                    self.continuehod = False
                    return
                else:
                    return
            else:
                return

        if self.ruleTwo(i,j):
            self.ipos = i
            self.jpos = j
            self.continuehod = True

        elif self.continuehod and (self.polemass[self.ipos][self.jpos] == 'q' or self.polemass[self.ipos][self.jpos]=='v'):
            self.hod(self.ipos, self.jpos, i, j)
            self.continuehod = False
            self.changeGoChess()

        elif self.continuehod and self.normalHodRule(self.ipos, self.jpos, i, j):
            self.hod(self.ipos, self.jpos, i, j)
            if self.damkaCheckWithoutEnemy(i, j):
                self.setDamka(i, j)
            self.continuehod = False
            self.changeGoChess()

    def hodWithEnemyForDamka(self, i, j):
        self.ienemy = 0
        self.jenemy = 0

        if i - self.ipos < 0:
            self.ienemy = i + 1
            if j - self.jpos < 0:
                self.jenemy = j + 1
            else:
                self.jenemy = j - 1
        else:
            self.ienemy = i - 1
            if j - self.jpos > 0:
                self.jenemy = j - 1
            else:
                self.jenemy = j + 1

        self.polemass[i][j] = self.polemass[self.ipos][self.jpos]
        self.polemass[self.ipos][self.jpos] = '.'
        self.polemass[self.ienemy][self.jenemy] = '.'

    def accesHodForDamka(self, i, j):
        mass=self.checkEnemyForDamka(self.ipos, self.jpos)
        self.ienemy = 0
        self.jenemy = 0

        if i - self.ipos < 0:
            self.ienemy = i + 1
            if j - self.jpos < 0:
                self.jenemy = j + 1
            else:
                self.jenemy = j - 1
        else:
            self.ienemy = i - 1
            if j - self.jpos > 0:
                self.jenemy = j - 1
            else:
                self.jenemy = j + 1

        if (self.ienemy, self.jenemy) in mass:
            return True
        else:
            return False


    def checkEnemyForDamka(self, i, j):
        ipos = i
        jpos = j
        enemymass = []
        for k in range(9):
            for a in (1, -1):
                for b in (1, -1):
                    print('[' + str(ipos - a * k) + "][" + str(jpos - b * k) + "]")
                    if ipos - a * k > 0  and jpos - b * k > 0 and ipos - a * k < 9 and jpos - b * k < 9:

                        if self.polemass[ipos - a * k][jpos - b * k] != "." and self.ruleOne(ipos - a * k,
                                                                                                 jpos - b * k) and self.polemass[ipos - a * (k+1)][jpos - b * (k+1)] == ".":
                            enemymass.append((ipos - a * k,jpos - b * k))


        return enemymass

    def ruleOne(self, i, j):

        if self.gochess == 'w':
            if self.polemass[i][j] == 'b' or self.polemass[i][j] == 'v':
                return True
            else:
                return False
        else:
            if self.polemass[i][j] == 'w' or self.polemass[i][j] == 'q':
                return True
            else:
                return False

    def ruleTwo(self, i, j):

        if self.gochess == 'b':
            if self.polemass[i][j] == 'b' or self.polemass[i][j] == 'v':
                return True
            else:
                return False
        else:
            if self.polemass[i][j] == 'w' or self.polemass[i][j] == 'q':
                return True
            else:
                return False
    def setDamka(self, i, j):
        if self.gochess == "w":
            self.polemass[i][j] = "q"
        else:
            self.polemass[i][j] = "v"

    def damkaCheckAfterEnemy(self, i, j):
        mass = self.checkEnemy(i, j)
        if len(mass) != 0:
            return False
        elif self.playerchess == "w":
            if self.gochess == "w" and i == 0:
                return True
            elif self.gochess == "b" and i == 9:
                return True
        else:
            if self.gochess == "b" and i == 0:
                return True
            elif self.gochess == "w" and i == 9:
                return True

        return False

    def damkaCheckWithoutEnemy(self, i, j):

        if self.playerchess == "w":
            if self.gochess == "w" and i == 0:
                return True
            elif self.gochess == "b" and i == 9:
                return True
        else:
            if self.gochess == "b" and i == 0:
                return True
            elif self.gochess == "w" and i == 9:
                return True

        return False

    def hodWithEnemy(self, i, j):
        self.ienemy = 0
        self.jenemy = 0

        if i - self.ipos < 0:
            self.ienemy = i + 1
            if j - self.jpos < 0:
                self.jenemy = j + 1
            else:
                self.jenemy = j - 1
        else:
            self.ienemy = i - 1
            if j - self.jpos > 0:
                self.jenemy = j - 1
            else:
                self.jenemy = j + 1

        self.polemass[i][j] = self.polemass[self.ipos][self.jpos]
        self.polemass[self.ipos][self.jpos] = '.'
        self.polemass[self.ienemy][self.jenemy] = '.'

        self.changeNumber()

    def accessHodWithEnemy(self,i,j):
        enemymass = []
        self.ienemy=0
        self.jenemy=0
        if i - self.ipos < 0:
            self.ienemy = i + 1
            if j - self.jpos < 0:
                self.jenemy = j + 1
            else:
                self.jenemy = j - 1
        else:
            self.ienemy = i - 1
            if j - self.jpos > 0:
                self.jenemy = j - 1
            else:
                self.jenemy = j + 1

        if self.polemass[self.ienemy][self.jenemy] == ".":
            return []
        for a in (2, -2):
            for b in (2, -2):
                try:
                    if self.polemass[self.ipos - a][self.jpos - b] != self.gochess:
                        enemymass.append((self.ipos - a, self.jpos - b))
                except Exception:
                    continue

        return enemymass

    def checkEnemy(self, i, j):
        enemymass = []

        for a in (1, -1):
            for b in (1, -1):
                try:
                    if i - a < 0 or i - a > 9 or j - b < 0 or j - b > 9 or i - a * 2 < 0 or i - a * 2 > 9 or j - b * 2 < 0 or j - b * 2 > 9:
                        continue
                    if self.polemass[i - a][j - b] != '.' and self.polemass[i - a][j - b] != self.polemass[i][j] and \
                                    self.polemass[i - a * 2][j - b * 2] == '.':
                        enemymass.append((i - a, j - b))
                except Exception:
                    continue

        return enemymass

    def checkChessWithEnemy(self):
        enemymass = []

        for i in range(10):
            for j in range(10):
                if self.gochess == "w" and self.polemass[i][j] == "q":
                    if len(self.checkEnemyForDamka(i, j)) != 0:
                        enemymass.append((i, j))
                        continue
                elif self.gochess == "b" and self.polemass[i][j] == "v":
                    if len(self.checkEnemyForDamka(i, j)) != 0:
                        enemymass.append((i, j))
                        continue
                if self.polemass[i][j] == self.gochess:
                    mass = self.checkEnemy(i, j)
                    if len(mass) != 0:
                        enemymass.append((i, j))
                else:
                    continue

        return enemymass

    def normalHodRule(self, ipos, jpos, i, j):
        if self.polemass[i][j]!='.':
            return False
        if abs(i - ipos) == 1 and abs(j - jpos) == 1:
            if self.playerchess == 'w':
                if self.gochess == 'w':
                    if (i - ipos) > 0:
                        return False
                    else:
                        return True
                elif self.gochess == 'b':
                    if (i - ipos) < 0:
                        return False
                    else:
                        return True
            elif self.playerchess == 'b':
                if self.gochess == 'w':
                    if (i - ipos) < 0:
                        return False
                    else:
                        return True
                elif self.gochess == 'b':
                    if (i - ipos) > 0:
                        return False
                    else:
                        return True
        else:
            return False

    def changeNumber(self):
        """
        Изменяет количество шашек на игровом столе
        """
        print(self.playerchess)
        if self.how_kill() == "w":
            self.numberOfWhite -= 1
        else:
            self.numberOfBlack -= 1
        print(str(self.numberOfWhite) + "|" + str(self.numberOfBlack))

    def endGame(self):
        """
        Проверка на конец игры
        :return: Tupel закончена ли игра и выиграл ли игрок
        """
        ishod = False
        endgame = False
        if self.numberOfBlack == 0 or self.numberOfWhite == 0:
            if self.numberOfWhite == 0:
                if self.playerchess == "w":
                    ishod = "lose"
                else:
                    ishod = "win"
            elif self.numberOfBlack == 0:
                if self.playerchess == "w":
                    ishod = "win"
                else:
                    ishod = "lose"
        return endgame, ishod

    # with test
    def how_kill(self):
        """
        функция для распознования цвета последней сбитой шашки
        :return: цвет сбитой шишки "black" or "white"
        """
        if self.gochess == "b":
            return "w"
        elif self.gochess == "w":
            return "b"

    def hod(self, ipos, jpos, i, j):
        """
        производит простой ход пешки
        :param ipos: начальная позиция 1
        :param jpos: начальная позиция 2
        :param i: куда ходит 1
        :param j: куда ходит 2
        :return: заполняет массив передеанный массив
        """
        self.polemass[i][j] = self.polemass[ipos][jpos]
        self.polemass[ipos][jpos] = '.'

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
                if (j * self.lengthOrWidth < mp[0] < (
                                j * self.lengthOrWidth + self.lengthOrWidth) and i * self.lengthOrWidth < mp[1] <
                    (i * self.lengthOrWidth + self.lengthOrWidth)):
                    return i, j

    def startpos(self, side='down'):
        """
        Задает массив доски с шашками
        :param side: сторона игрока down или up
        :return: ничего не возвращает тк заполняет преданный массив
        """

        if side == 'down':
            self.polemass = [
                list(' b b b b b'),
                list('b b b b b '),
                list(' b b b b b'),
                list('b b b b b '),
                list(' . . . . .'),
                list('. . b . . '),
                list(' w w w w w'),
                list('w w w w w '),
                list(' w w w w w'),
                list('w w w w w '),
            ]

        elif side == 'up':
            self.polemass = [
                list(' w w w w w'),
                list('w w w w w '),
                list(' w w w w w'),
                list('w w w w w '),
                list(' . . . . .'),
                list('. . . . . '),
                list(' b b b b b'),
                list('b b b b b '),
                list(' b b b b b'),
                list('b b b b b '),
            ]

    def changeGoChess(self):
        if self.gochess == 'w':
            self.gochess = 'b'
        else:
            self.gochess = 'w'


