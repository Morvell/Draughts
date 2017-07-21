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






