from collections import OrderedDict

class Cache(object):

    def __init__(self, capacity):
        self.orderedDict = OrderedDict()
        self.capacity = capacity

    def add(self, key, value):
        if len(self.orderedDict) >= self.capacity:
            self.orderedDict.popitem(last = False)
        self.orderedDict[key] = value

    def get(self, key):
        if key is None:
            return -1
        
        val = self.orderedDict.get(key, -1)
        if val == -1:
            return val
        else:
            return self.orderedDict[key]

    def printDict(self):
        print(self.orderedDict)


# Test case 1
cache = Cache(3)

cache.add(1, 1)
cache.add(2, 2)
cache.add(3, 3)

cache.printDict()

cache.add(5, 5)
cache.get(4)
cache.printDict()

# Test case 2
cache = Cache(6)

cache.add(1, 1)
cache.add(2, 2)
cache.add(3, 3)
cache.add(4, 4)
cache.add(5, 5)
cache.get(3)

cache.printDict()

cache.add(6, 6)
cache.get(4)
cache.printDict()

# Test case 3
cache = Cache(1)

cache.add(1, 1)
cache.get(1)

cache.printDict()

cache.add(2, 2)
cache.get(2)
cache.printDict()