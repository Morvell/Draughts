class HistoryArray:
    def __init__(self, n):
        self.n = n
        self.array = []

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

    def __len__(self):
        return len(self.array)
