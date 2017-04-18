# -*- coding: utf-8 -*-
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
        from main import polemass
        self.s.sendto(
            json.dumps(polemass).encode(),
            (netveriable.SEND_IP, netveriable.SEND_PORT))
    def next_hod(self):
        from main import polemass
        self.s.sendto(
            json.dumps(('next',polemass)).encode(),
            (netveriable.SEND_IP, netveriable.SEND_PORT))


class Server:
    """
    Сервер. Получает данные с других сокетов и обрабатывает их
    """

    def __init__(self):
        """
        инициализирут сокет для получения данных
        """

        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            import threading
            threading.Thread(target=self.new_thread).start()
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

    def new_thread(self):
        """
        получает данные и обрабатывает их. если поевляется новый пользователь,
        отправляет существующим новый список участников
        А так же обрабатывает получение файла
        """
        try:
            self.streamdata = self.s.recvfrom(1024)
            self.data = json.loads(self.streamdata[0].decode())
            self.addr = self.streamdata[1]

            if isinstance(self.data, list) and len(self.data) == 2 and self.data[0]=='ready':

                netveriable.ENEMY_NICKNAME = self.data[1]
                self.s.sendto(json.dumps(('ready',netveriable.NICKNAME)).encode(),
                              (netveriable.SEND_IP,netveriable.SEND_PORT))
                netveriable.ENEMY_READY = True
            elif isinstance(self.data, list) and len(self.data) == 2 and self.data[0]=='next':
                from main import gochess,playerchess,polemass
                global polemass
                global gochess
                global playerchess
                polemass = self.data[1]
                gochess=playerchess
            elif isinstance(self.data, list) and len(self.data) == 1:

                polemass=self.data

            elif isinstance(self.data, str) and self.data=='exit':

                netveriable.ENEMY_READY = False
                netveriable.NETWORK_READY = False

        except Exception:
            print('Exeption')

