class OrderedStream:

    def __init__(self, n):
        self.n = n
        self.values = [None] * n
        self.ptr = 0

    def insert(self, idKey, value):
        self.values[idKey - 1] = value
        
        chunk = []
        while self.ptr < self.n and self.values[self.ptr] is not None:
            chunk.append(self.values[self.ptr])
            self.ptr += 1
        
        return chunk