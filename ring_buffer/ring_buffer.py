class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None] * capacity
        self.tail = -1
        self.head = 0
        self.size = 0

    def append(self, item):
        if self.size == self.capacity:
            print('RB is full')
            return None

        else:
            self.tail = (self.tail + 1) % self.capacity
            self.data[self.tail] = item
            self.size += 1

    def get(self):
        return self.data
