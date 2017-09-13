class HahkiAPI:
    def __init__(self):
        self.numberOfWhite = 20
        self.numberOfBlack = 20

        self.WHITE_DRAUGHT = 'w'
        self.WHITE_KING = 'q'
        self.BLACK_DRAUGHT = 'b'
        self.BLACK_KING = 'v'
        self.GAME_PIECE = '.'
        self.NOGAME_PIECE = ' '
        self.SIDE_UP = 'up'
        self.SIDE_DOWN = 'down'

        self.lastKill = self.GAME_PIECE

        self.gameSide = self.SIDE_UP
        self.playerDraughts = self.WHITE_DRAUGHT
        self.playDraughts = self.WHITE_DRAUGHT
        self.AI = False

        self.gameField = []

        self.mouseButtonDownFlag = False
        self.continueStep = False
        self.continueDraught = None

        # iFirstActivePosition, jFirstActivePosition = позиция шашки на которую иначально выбрали для действий с ней
        self.iFirstActivePosition = 0
        self.jFirstActivePosition = 0

        self.LENGTH_OR_WIDTH = 72

    def without_net(self, mp):
        """
        Распределяет на игру с ии и без
        :param mp: координаты мышки
        """

        if self.AI and self.playDraughts != self.playerDraughts:
            for i in range(10):
                if self.playDraughts != self.playerDraughts:
                    for j in range(10):
                        self.game_logic(i, j)
        else:
            i, j = self.check_draughts(mp)
            self.game_logic(i, j)

    def game_logic(self, i, j):
        """
        обработка всех игровых событий
        :param i: первый индекс массива
        :param j: второй индекс массива
        """
        # проверка что бы не ходил на пустую клетку
        if self.gameField[i][j] == self.GAME_PIECE and self.continueStep == False:
            return

        draughts_with_enemy = self.check_chess_with_enemy()
        if len(draughts_with_enemy) != 0:
            if (i, j) in draughts_with_enemy:
                self.iFirstActivePosition = i
                self.jFirstActivePosition = j
                self.continueStep = True
                return

            if self.continueStep and self.king_or_not_king() and self.correct_hod_for_king(i, j):
                self.step_with_enemy_for_king(i, j)
                if len(self.check_chess_with_enemy()) == 0:
                    self.change_godraught()
                    self.continueStep = False
                    return
                else:
                    return

            if self.continueStep and (i, j) in self.correct_step_with_enemy(i, j):
                self.step_with_enemy(i, j)
                if i == 0 or i == 9:
                    if self.king_check_after_enemy(i, j):
                        self.set_king(i, j)
                if len(self.check_chess_with_enemy()) == 0:
                    self.change_godraught()
                    self.continueStep = False
                    return
                else:
                    return
            else:
                return

        if self.friend_or_not(i, j):
            self.iFirstActivePosition = i
            self.jFirstActivePosition = j
            self.continueStep = True

        elif self.continueStep and self.king_or_not_king():
            self.simple_step(self.iFirstActivePosition, self.jFirstActivePosition, i, j)
            self.continueStep = False
            self.change_godraught()

        elif self.continueStep and self.normal_step_rule(self.iFirstActivePosition, self.jFirstActivePosition, i, j):
            self.simple_step(self.iFirstActivePosition, self.jFirstActivePosition, i, j)
            if self.king_check_without_enemy(i):
                self.set_king(i, j)
            self.continueStep = False
            self.change_godraught()

    def step_with_enemy_for_king(self, i, j):
        """
        реализация хода для короля
        :param i: первая позиция для хода
        :param j: вторая позиция для хода
        """
        self.i_enemy_position = 0
        self.j_enemy_position = 0

        if i - self.iFirstActivePosition < 0:
            self.i_enemy_position = i + 1
            if j - self.jFirstActivePosition < 0:
                self.j_enemy_position = j + 1
            else:
                self.j_enemy_position = j - 1
        else:
            self.i_enemy_position = i - 1
            if j - self.jFirstActivePosition > 0:
                self.j_enemy_position = j - 1
            else:
                self.j_enemy_position = j + 1

        self.gameField[i][j] = self.gameField[self.iFirstActivePosition][self.jFirstActivePosition]
        self.gameField[self.iFirstActivePosition][self.jFirstActivePosition] = self.GAME_PIECE
        self.gameField[self.i_enemy_position][self.j_enemy_position] = self.GAME_PIECE
        self.change_number_of_live_draughts()

    def correct_hod_for_king(self, i, j):
        """
        проверка правельности хода для короля
        :param i: первая позиция выбранной шашки
        :param j: вторая позиция выбранной шашки
        :return: True or False
        """
        mass = self.check_enemy_for_king(self.iFirstActivePosition, self.jFirstActivePosition)
        self.i_enemy_position = 0
        self.j_enemy_position = 0

        if i - self.iFirstActivePosition < 0:
            self.i_enemy_position = i + 1
            if j - self.jFirstActivePosition < 0:
                self.j_enemy_position = j + 1
            else:
                self.j_enemy_position = j - 1
        else:
            self.i_enemy_position = i - 1
            if j - self.jFirstActivePosition > 0:
                self.j_enemy_position = j - 1
            else:
                self.j_enemy_position = j + 1

        if (self.i_enemy_position, self.j_enemy_position) in mass:
            return True
        else:
            return False

    def king_or_not_king(self):
        """
        Проверка на короля
        :return: True or False
        """
        if self.gameField[self.iFirstActivePosition][self.jFirstActivePosition] == self.WHITE_KING or \
                        self.gameField[self.iFirstActivePosition][self.jFirstActivePosition] == self.BLACK_KING:
            return True
        else:
            return False

    def check_enemy_for_king(self, i, j):
        """
        Нахождение врагов для короля
        :param i: первая позиция выбранной шашки
        :param j: вторая позиция выбранной шашки
        :return: массив с позициями возможных врагов
        """
        i_first_position = i
        j_first_position = j
        enemy_array = []
        for k in range(9):
            for a in (1, -1):
                for b in (1, -1):
                    # print('[' + str(iFirstActivePosition - a * k) + "][" + str(jFirstActivePosition - b * k) + "]")
                    if i_first_position - a * k > 0 and j_first_position - b * k > 0 and i_first_position - a * k < 9 and j_first_position - b * k < 9:

                        if self.gameField[i_first_position - a * k][
                                    j_first_position - b * k] != "." and self.enemy_or_not(
                                        i_first_position - a * k,
                                        j_first_position - b * k) and \
                                        self.gameField[i_first_position - a * (k + 1)][
                                                    j_first_position - b * (k + 1)] == ".":
                            enemy_array.append((i_first_position - a * k, j_first_position - b * k))

        return enemy_array

    def enemy_or_not(self, i, j):
        """
        проверка на врага
        :param i: первая позиция проверяемой шишки
        :param j: вторая позиция проверяемой шашки
        :return: True or False
        """
        if self.playDraughts == 'w':
            if self.gameField[i][j] == 'b' or self.gameField[i][j] == 'v':
                return True
            else:
                return False
        else:
            if self.gameField[i][j] == 'w' or self.gameField[i][j] == 'q':
                return True
            else:
                return False

    def friend_or_not(self, i, j):
        """
        Проверка на друга
        :param i: первая позиция проверяемой шашки
        :param j: вторая позиция проверяемой шашки
        :return: True or False
        """
        if self.playDraughts == 'b':
            if self.gameField[i][j] == 'b' or self.gameField[i][j] == 'v':
                return True
            else:
                return False
        else:
            if self.gameField[i][j] == 'w' or self.gameField[i][j] == 'q':
                return True
            else:
                return False

    def set_king(self, i, j):
        """
        Установка короля в массиве поля
        :param i: первая позиция замеяемой шашки
        :param j: вторая позиция заменяемой шашки
        """
        if self.playDraughts == "w":
            self.gameField[i][j] = "q"
        else:
            self.gameField[i][j] = "v"

    def king_check_after_enemy(self, i, j):
        """
        проверка на возможность замены на короля после срубания шашки
        :param i: первая позиция проверяемой шашки
        :param j: вторая позиция проверяемой шашки
        :return: True or False
        """
        mass = self.check_enemy(i, j)
        if len(mass) != 0:
            return False
        else:
            return self.king_check_without_enemy(i)

    def king_check_without_enemy(self, i):
        """
        проверка на возможность замены на короля после простого хода
        :param i: позиция шашки по горизонтали
        :return: True or False
        """
        if self.playerDraughts == "w":
            if self.playDraughts == "w" and i == 0:
                return True
            elif self.playDraughts == "b" and i == 9:
                return True
        else:
            if self.playDraughts == "b" and i == 0:
                return True
            elif self.playDraughts == "w" and i == 9:
                return True

        return False

    def step_with_enemy(self, i, j):
        """
        реализация хода через врага
        :param i: первая позиция куда ходить
        :param j: вторая позиция куда ходить
        """
        self.i_enemy_position = 0
        self.j_enemy_position = 0

        if i - self.iFirstActivePosition < 0:
            self.i_enemy_position = i + 1
            if j - self.jFirstActivePosition < 0:
                self.j_enemy_position = j + 1
            else:
                self.j_enemy_position = j - 1
        else:
            self.i_enemy_position = i - 1
            if j - self.jFirstActivePosition > 0:
                self.j_enemy_position = j - 1
            else:
                self.j_enemy_position = j + 1

        self.gameField[i][j] = self.gameField[self.iFirstActivePosition][self.jFirstActivePosition]
        self.gameField[self.iFirstActivePosition][self.jFirstActivePosition] = '.'
        self.gameField[self.i_enemy_position][self.j_enemy_position] = '.'

        self.change_number_of_live_draughts()

    def correct_step_with_enemy(self, i, j):
        """
        выдает массив с нужными врагами
        """
        if self.gameField[i][j] != self.GAME_PIECE:
            return []
        enemy_array = []
        self.i_enemy_position = 0
        self.j_enemy_position = 0
        if i - self.iFirstActivePosition < 0:
            self.i_enemy_position = i + 1
            if j - self.jFirstActivePosition < 0:
                self.j_enemy_position = j + 1
            else:
                self.j_enemy_position = j - 1
        else:
            self.i_enemy_position = i - 1
            if j - self.jFirstActivePosition > 0:
                self.j_enemy_position = j - 1
            else:
                self.j_enemy_position = j + 1

        if not self.out_of_range(self.i_enemy_position, self.j_enemy_position) or self.gameField[self.i_enemy_position][self.j_enemy_position] == self.playDraughts:
            return []
        if self.out_of_range(self.i_enemy_position, self.j_enemy_position) and self.gameField[self.i_enemy_position][
            self.j_enemy_position] == ".":
            return []
        for a in (2, -2):
            for b in (2, -2):
                try:
                    if self.gameField[self.iFirstActivePosition - a][
                                self.jFirstActivePosition - b] != self.playDraughts:
                        enemy_array.append((self.iFirstActivePosition - a, self.jFirstActivePosition - b))
                except Exception:
                    continue

        return enemy_array

    def out_of_range(self, i, j):
        """
        проверка на out of range
        :param i:
        :param j:
        :return: True or False
        """
        if i < 0 or i > 9 or j < 0 or j > 9:
            return False
        return True

    def check_enemy(self, i, j):
        """
        находит всех врагов
        :param i: первая позиция проверяемой шашки
        :param j: вторая позиция проверяемой шашки
        :return: массив с врагами
        """
        enemy_array = []

        for a in (1, -1):
            for b in (1, -1):
                try:
                    if i - a < 0 or i - a > 9 or j - b < 0 or j - b > 9 or i - a * 2 < 0 or i - a * 2 > 9 or j - b * 2 < 0 or j - b * 2 > 9:
                        continue
                    if self.gameField[i - a][j - b] != '.' and self.gameField[i - a][j - b] != self.gameField[i][j] and \
                                    self.gameField[i - a * 2][j - b * 2] == '.':
                        enemy_array.append((i - a, j - b))
                except Exception:
                    continue

        return enemy_array

    def check_chess_with_enemy(self):
        """
        нахождение всех шашек с врагами
        :return: массив шашек с врагами
        """
        enemy_array = []

        for i in range(10):
            for j in range(10):
                if self.playDraughts == "w" and self.gameField[i][j] == "q":
                    if len(self.check_enemy_for_king(i, j)) != 0:
                        enemy_array.append((i, j))
                        continue
                elif self.playDraughts == "b" and self.gameField[i][j] == "v":
                    if len(self.check_enemy_for_king(i, j)) != 0:
                        enemy_array.append((i, j))
                        continue
                if self.gameField[i][j] == self.playDraughts:
                    mass = self.check_enemy(i, j)
                    if len(mass) != 0:
                        enemy_array.append((i, j))
                else:
                    continue

        return enemy_array

    def normal_step_rule(self, i_first_position, j_first_position, i, j):
        """
        Проверка на правельность простого хода
        :param i_first_position: первая позиция чем ходят
        :param j_first_position: вторая позиция чем ходят
        :param i: первая позиция куда пойдут
        :param j: вторая позиция куда пойдут
        :return: True or False
        """
        if self.gameField[i][j] != '.':
            return False
        if abs(i - i_first_position) == 1 and abs(j - j_first_position) == 1:
            if self.playerDraughts == 'w':
                if self.playDraughts == 'w':
                    if (i - i_first_position) > 0:
                        return False
                    else:
                        return True
                elif self.playDraughts == 'b':
                    if (i - i_first_position) < 0:
                        return False
                    else:
                        return True
            elif self.playerDraughts == 'b':
                if self.playDraughts == 'w':
                    if (i - i_first_position) < 0:
                        return False
                    else:
                        return True
                elif self.playDraughts == 'b':
                    if (i - i_first_position) > 0:
                        return False
                    else:
                        return True
        else:
            return False

    def change_number_of_live_draughts(self):
        """
        Изменяет количество шашек на игровом столе
        """
        print(self.playerDraughts)
        if self.who_was_killed() == "w":
            self.numberOfWhite -= 1
        else:
            self.numberOfBlack -= 1
        print(str(self.numberOfWhite) + "|" + str(self.numberOfBlack))

    def check_end_game(self):
        """
        Проверка на конец игры
        :return: Tupel закончена ли игра и выиграл ли игрок
        """
        game_result = False
        end_game = False
        if self.numberOfBlack == 0 or self.numberOfWhite == 0:
            if self.numberOfWhite == 0:
                if self.playerDraughts == "w":
                    game_result = "lose"
                else:
                    game_result = "win"
            elif self.numberOfBlack == 0:
                if self.playerDraughts == "w":
                    game_result = "win"
                else:
                    game_result = "lose"
        return end_game, game_result

    def who_was_killed(self):
        """
        функция для распознования цвета последней сбитой шашки
        :return: цвет сбитой шишки "black" or "white"
        """
        if self.playDraughts == "b":
            return "w"
        elif self.playDraughts == "w":
            return "b"

    def simple_step(self, i_first_position, j_first_position, i, j):
        """
        производит простой ход пешки
        :param i_first_position: начальная позиция 1
        :param j_first_position: начальная позиция 2
        :param i: куда ходит 1
        :param j: куда ходит 2
        """
        self.gameField[i][j] = self.gameField[i_first_position][j_first_position]
        self.gameField[i_first_position][j_first_position] = '.'

    def check_draughts(self, mp):
        """
        производит проверку на принадлежность указателя мыши клетке на доске
        :param mp: данные о указатели мыши
        :return: True если мышь находится на i и j  позиции или False в противном
        """
        for i in range(10):
            for j in range(10):
                if (j * self.LENGTH_OR_WIDTH < mp[0] and mp[0] < (
                                j * self.LENGTH_OR_WIDTH + self.LENGTH_OR_WIDTH) and i * self.LENGTH_OR_WIDTH < mp[
                    1] and mp[1] <
                    (i * self.LENGTH_OR_WIDTH + self.LENGTH_OR_WIDTH)):
                    return i, j
        return 0, 0

    def set_start_playing_field(self, side='down'):
        """
        Задает массив доски с шашками
        :param side: сторона игрока down или up
        :return: ничего не возвращает тк заполняет преданный массив
        """

        if side == 'down':
            self.gameField = [
                list(' . . . v .'),
                list('. . . . . '),
                list(' . . . . .'),
                list('. . . . . '),
                list(' . . b . .'),
                list('. . . . . '),
                list(' . . . . .'),
                list('. w . . . '),
                list(' b . . . .'),
                list('. . . . . '),
            ]

        elif side == 'up':
            self.gameField = [
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

    def change_godraught(self):
        """
        изменяет цвет шашек которыми нужно ходить
        """
        if self.playDraughts == 'w':
            self.playDraughts = 'b'
        else:
            self.playDraughts = 'w'
