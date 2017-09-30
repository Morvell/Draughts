class HistoryArray:
    def __init__(self, n):
        self.n = n
        self.array = []

    def set_array(self, string):
        first_reparse = string.split("@")
        self.n = int(first_reparse[0])
        second_reparse = first_reparse[1].split("+")
        for i in second_reparse:
            if i == "":
                continue
            r = i.split("!")
            self.array.append(((int(r[0][1]), int(r[0][4])), (int(r[1][1]), int(r[1][4])), r[2]))

    def put(self, object):
        self.array.append(object)
        if len(self.array) > self.n:
            self.array.pop(0)

    def get_first(self, n):
        return self.array[n][0]

    def get_second(self, n):
        return self.array[n][1]

    def get_color(self, n):
        return self.array[n][2]

    def get_element(self, n):
        return self.array[n]

    def __len__(self):
        return len(self.array)

    def __str__(self):
        string = str(self.n) + '@'
        for i in range(len(self.array)):
            string += str(self.get_first(i)) + "!" + str(self.get_second(i)) + "!" + str(self.get_color(i)) + "+"
        return string
