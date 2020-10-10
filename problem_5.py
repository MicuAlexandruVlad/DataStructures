import hashlib
import datetime

class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None

    def calc_hash(self):
        sha = hashlib.sha256()

        hash_str = self.data.encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()

class Chain:

    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        if data != "" or data is not None:
            if self.head is None:
                self.head = Block(datetime.datetime.utcnow(), data, 0)
                self.tail = self.head
            else:
                self.tail.next = Block(datetime.datetime.utcnow(), data, self.tail.hash)
                self.tail = self.tail.next

    def print(self):
        l = []
        block = self.head
        while block:
            l.append([block])
            block = block.next
        return l


def test(length):
    c = Chain()
    for i in range(length):
        data = "data" + str(i)
        c.insert(data)
    
    return c

print(test(10).print())
print(test(1).print())
print(test(4).print())



