class HistaryArray:
    def __init__(self, n):
        self.n = n
        self.array = []


    def put(self, object):
        if len(self.array) < self.n:
            self.array.append(object)
        elif len(self.array) == self.n:
            clon = self.array.copy()
            self.array[0] = object
            for i in range (1, self.n):
                self.array[i] = clon[i-1]

    def get(self,n):
        return self.array[n]

    def __len__(self):
        return len(self.array)
