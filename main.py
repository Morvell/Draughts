# -*- coding: utf-8 -*-
import pygame, sys
from netwindow import enterwindow
import netveriable
import Net
import Hahki
from Hahkiapi import *
import threading
import socket

pygame.init()

import copy

SRV = None
CLT = None
tsrv = None
tclt = None

import socket
import sys
import json
import netveriable


class Client:
    """
    Класс клиент. Осуществляет отправку данных
    """

    def __init__(self):
        """
        Создает сокет и отправляет сокету-получателю свои данные(порт и ip)
        """
        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            self.s.bind((netveriable.YOUR_IP, netveriable.YOUR_PORT))
        except socket.error:
            print('Failed to create socket')
            sys.exit()

        self.s.sendto(
            json.dumps(('ready', netveriable.NICKNAME)).encode(),
            (netveriable.SEND_IP, netveriable.SEND_PORT))
        print("You may send are message")

    def send_array(self):
        """
        обрабатывает ввод сообщения,
        файла и отправляет сообшение всем подключенным пользователям
        """
        global polemass
        mass = self.polemassparser(polemass)
        self.s.sendto(
            json.dumps(mass).encode(),
            (netveriable.SEND_IP, netveriable.SEND_PORT))

    def next_hod(self):
        """
        отравляет опоненту ообщение о том что он может начинать ходить
        """
        global polemass
        mass = self.polemassparser(polemass)
        self.s.sendto(
            json.dumps(('next', mass)).encode(),
            (netveriable.SEND_IP, netveriable.SEND_PORT))

    def polemassparser(self, mass):
        """
        парсит массив классов в массив строк для передачи по сети
        :param mass: массив который надо парсить(с данными о доске)
        :return итоговый распарсенный массив
        """
        self.polemass = []
        for i in range(10):
            self.polemass.append([])
            for j in range(10):
                self.polemass[i].append([])

        for i in range(10):
            for j in range(10):
                if type(mass[i][j]) == Hahki.Kletka:
                    self.polemass[i][j] = ("Kletka|" + str(mass[i][j].x) + '|' + str(mass[i][j].y))
                else:
                    self.polemass[i][j] = (
                    "Hahka|" + str(mass[i][j].x) + '|' + str(mass[i][j].y) + '|' + str(mass[i][j].vid) + '|' +
                    str(mass[i][j].side) + '|' + str(mass[i][j].damka))
        return self.polemass


class Server(threading.Thread):
    """
    Сервер. Получает данные с других сокетов и обрабатывает их
    """

    def __init__(self):
        """
            инициализирут сокет для получения данных
            """
        super().__init__()
        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            print('Socket created')
        except socket.error as msg:
            print('Failed to create socket. Error Code : ')
            sys.exit()
        try:
            self.s.bind((netveriable.YOUR_IP, netveriable.YOUR_PORT))
        except socket.error as msg:
            print('Bind failed. Error Code : ')
            sys.exit()
        print('Socket bind complete')

    def run(self):
        """
        получает данные и обрабатывает их. если поевляется новый пользователь,
        отправляет существующим новый список участников
        А так же обрабатывает получение файла
        """
        print('1')
        while True:
            try:
                self.streamdata = self.s.recvfrom(4096)
                self.data = json.loads(self.streamdata[0].decode())
                self.addr = self.streamdata[1]

                if isinstance(self.data, list) and len(self.data) == 2 and self.data[0] == 'ready':

                    netveriable.ENEMY_NICKNAME = self.data[1]
                    self.s.sendto(json.dumps(('ready', netveriable.NICKNAME)).encode(),
                                  (netveriable.SEND_IP, netveriable.SEND_PORT))
                    netveriable.ENEMY_READY = True
                elif isinstance(self.data, list) and len(self.data) == 2 and self.data[0] == 'next':
                    print('next')

                    global polemass
                    global gochess
                    global playerchess
                    self.polemassdeparser(self.data[1], polemass)
                    gochess = playerchess
                elif isinstance(self.data, list) and len(self.data) == 1:

                    self.polemassdeparser(self.data, polemass)

                elif isinstance(self.data, str) and self.data == 'exit':

                    netveriable.ENEMY_READY = False
                    netveriable.NETWORK_READY = False

            except Exception as e:
                print(e)

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


class Menu(threading.Thread):
    def __init__(self, punkts=(300, 300, u'start', (123, 235, 34), (34, 25, 66), 1)):
        super().__init__()
        self.i_menu = pygame.image.load('pic\menu.png')
        self.i_rmenu = pygame.image.load('pic\menurightscreen.png')
        self.punkts = punkts

    def render(self, poverhnost, font, num_punkt):
        for e in self.punkts:
            if num_punkt == e[5]:
                poverhnost.blit(font.render(e[2], 1, e[4]), (e[0], e[1]))
            else:
                poverhnost.blit(font.render(e[2], 1, e[3]), (e[0], e[1]))

    def run(self):
        done = True
        font_menu = pygame.font.SysFont("comicsansms", 50)
        punkt = 0
        while done:
            # mainscreen.fill((0,100,200))

            mp = pygame.mouse.get_pos()

            for i in self.punkts:
                if mp[0] > i[0] and mp[0] < (i[0] + 155) and mp[1] > i[1] and mp[1] < (i[1] + 50):
                    punkt = i[5]
            self.render(mainscreen, font_menu, punkt)
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        sys.exit()
                    if e.key == pygame.K_UP:
                        if punkt > 0:
                            punkt -= 1
                    if e.key == pygame.K_DOWN:
                        if punkt < (len(self.punkts) - 1):
                            punkt += 1
                if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                    if punkt == 0:
                        done = False
                    elif punkt == 1:
                        enterwindow()
                        if netveriable.NETWORK_READY == True:
                            global SRV
                            global CLT
                            global tsrv
                            SRV = Server()
                            CLT = Client()
                            SRV.start()
                            while (not (SRV.isAlive())):
                                SRV.start()
                                print('no start thread')


                    elif punkt == 2:
                        sys.exit()

            window.blit(mainscreen, (0, 0))
            window.blit(rightscreen, (720, 0))
            mainscreen.blit(self.i_menu, (0, 0))
            rightscreen.blit(self.i_rmenu, (0, 0))
            pygame.display.flip()


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
                                                                               polemass[i][j]))) and polemass[i][
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


def with_net():
    global continuehod
    global mouse_button_down_fl
    global gochess
    global ipos
    global jpos
    global continuehahka
    if gochess == playerchess:
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
                                    CLT.next_hod()
                                    gochess = None
                                else:
                                    set_damka(polemass, i, j)
                                    continuehod = True
                                    continuehahka = polemass[i][j]
                                    CLT.send_array()
                                break


                        elif (check_hod_without_enemy(polemass[ipos][jpos], polemass[i][j]) or (
                            polemass[ipos][jpos].damka and check_correct_damka_hod(polemass[ipos][jpos],
                                                                                   polemass[i][j]))) and polemass[i][
                            j].vid == 'kletka':
                            print('in True')
                            mouse_button_down_fl = False
                            hod(polemass, ipos, jpos, i, j)
                            set_damka(polemass, i, j)
                            CLT.next_hod()
                            gochess = None
                            break


window = pygame.display.set_mode((920, 720))
pygame.display.set_caption(u"Hahki")
pygame.display.set_icon(pygame.image.load('pic\DBlack.gif').convert())
mainscreen = pygame.Surface((720, 720))
rightscreen = pygame.Surface((280, 720))

board = pygame.image.load('pic\Board.gif')
i_hb = pygame.image.load('pic\HBlack.gif')
i_hw = pygame.image.load('pic\HWhite.gif')
i_db = pygame.image.load('pic\DBlack.gif')
i_dw = pygame.image.load('pic\DWhite.gif')
i_rightscreen = pygame.image.load('pic\\rightscreen.png')

polemass = []
side = 'down'
startpos(polemass, side, (i_hb, i_hw, i_db, i_dw))
playerchess = 'white'
gochess = 'white'
done = True

mouse_button_down_fl = False
continuehod = False
continuehahka = None

ipos = 0
jpos = 0

punkts = [(400, 200, u'Start', (123, 15, 34), (235, 75, 156), 0),
          (400, 300, u'NetGame', (123, 15, 34), (235, 75, 156), 1),
          (400, 400, u'Exit', (123, 15, 34), (235, 75, 156), 2)]
game = Menu(punkts)
game.run()

while done:
    mp = pygame.mouse.get_pos()

    for e in pygame.event.get():

        if e.type == pygame.QUIT:
            done = False
        if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
            print(netveriable.NETWORK_READY)
            if netveriable.NETWORK_READY == False:
                print('2')
                without_net()
            elif netveriable.NETWORK_READY == True:
                print('3')
                with_net()

    window.blit(mainscreen, (0, 0))
    window.blit(rightscreen, (720, 0))
    rightscreen.blit(i_rightscreen, (0, 0))
    mainscreen.blit(board, (0, 0))

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
