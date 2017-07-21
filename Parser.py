import Hahki
from Hahkiapi import i_db, i_dw
from main import i_hb, i_hw


def polemassparser(mass):
    """
    парсит массив классов в массив строк для передачи по сети
    :param mass: массив который надо парсить(с данными о доске)
    :return итоговый распарсенный массив
    """
    polemass = []
    for i in range(10):
        polemass.append([])
        for j in range(10):
            polemass[i].append([])

    for i in range(10):
        for j in range(10):
            if type(mass[i][j]) == Hahki.Kletka:
                polemass[i][j] = ("Kletka|" + str(mass[i][j].x) + '|' + str(mass[i][j].y))
            else:
                polemass[i][j] = (
                    "Hahka|" + str(mass[i][j].x) + '|' + str(mass[i][j].y) + '|' + str(mass[i][j].vid) + '|' +
                    str(mass[i][j].side) + '|' + str(mass[i][j].damka))
    return polemass

def polemassdeparser(self, mass, polemass):
    """
    :param mass: массив полученный после polymassparser
    :param polemass: массив в который будем распарсевать
    """
    for i in range(10):
        for j in range(10):
            smass = mass[i][j].split('|')
            if smass[0] == 'Kletka':
                polemass[i][j] = Hahki.Kletka(int(smass[1]), int(smass[2]))
            else:
                if smass[3] == 'black' and smass[5] == 'False':
                    polemass[i][j] = Hahki.Hahka(int(smass[1]), int(smass[2]), 'black', i_hb, smass[4])
                    polemass[i][j].damka = False
                elif smass[3] == 'white' and smass[5] == 'False':
                    polemass[i][j] = Hahki.Hahka(int(smass[1]), int(smass[2]), 'white', i_hw, smass[4])
                    polemass[i][j].damka = False
                elif smass[3] == 'black' and smass[5] == 'True':
                    polemass[i][j] = Hahki.Hahka(int(smass[1]), int(smass[2]), 'black', i_db, smass[4])
                    polemass[i][j].damka = True
                elif smass[3] == 'white' and smass[5] == 'True':
                    polemass[i][j] = Hahki.Hahka(int(smass[1]), int(smass[2]), 'white', i_dw, smass[4])
                    polemass[i][j].damka = True




