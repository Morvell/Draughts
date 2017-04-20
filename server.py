
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


