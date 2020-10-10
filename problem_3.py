import sys
from collections import OrderedDict
huff = {}

class Node():
    # bit => 0 - left, 1 - right; symbol => letter
    def __init__(self, symbol, freq):
        self.symbol = symbol
        self.freq = freq
        self.left = None
        self.right = None


def computeFrequency(data):
    freqDict = {}
    for char in data:
        if char not in freqDict.keys():
            freqDict[char] = 1
        else:
            freqDict[char] += 1


    return sortDict(freqDict)

def sortDict(freqDict):
    return OrderedDict(sorted(freqDict.items(), key=lambda x: x[1]))

def popTwo(freqMap):
    entry1 = freqMap.popitem(last=False)
    entry2 = freqMap.popitem(last=False)
    node1 = Node(entry1[0], entry1[1])
    node2 = Node(entry2[0], entry2[1])
    sumNode = Node(None, node1.freq + node2.freq)
    if node1.freq >= node2.freq:
        sumNode.left = node2
        sumNode.right = node1
    else:
        sumNode.right = node2
        sumNode.left = node1

    return sumNode

def makeRoot(lsn, ln):
    root = Node(None, lsn.freq + ln.freq)

    if lsn.freq >= ln.freq:
        root.left = ln
        root.right = lsn
    else:
        root.left = lsn
        root.right = ln

    return root

def buildTree(data):
    freqMap = computeFrequency(data)
    print(freqMap)
    nodes = []
    root = None
    
    nodes.append(popTwo(freqMap))

    while len(freqMap) > 2:
        # entry = freqMap.popitem(last=False)
        # node = Node(entry[0], entry[1])
        node = popTwo(freqMap)

        lastInsertedNode = nodes[len(nodes) - 1]
        sn = Node(None, lastInsertedNode.freq + node.freq)

        if lastInsertedNode.freq >= node.freq:
            sn.left = node
            sn.right = lastInsertedNode
        else:
            sn.left = lastInsertedNode
            sn.right = node
        
        nodes.append(sn)

    if len(freqMap) > 1:
        lsn = popTwo(freqMap)

        ln = nodes[len(nodes) - 1]
        
        root = makeRoot(lsn, ln)
    elif len(freqMap) != 0:
        le = freqMap.popitem(last=False)
        ln = Node(le[0], le[1])

        lsn = nodes[len(nodes) - 1]
        root = makeRoot(lsn, ln)
    elif len(freqMap) == 0:
        root = nodes[len(nodes) - 1]
    return root

def buildHuff(root, bit):
    if root:
        buildHuff(root.left, bit + "0")

        if root.symbol is not None:
            huff[root.symbol] = bit

        buildHuff(root.right, bit + "1")

def huffman_encoding(data):
    
    if len(computeFrequency(data)) == 1:
        root = Node(None, len(data))
        node = Node(data[0], len(data))
        root.left = node
    else:
        root = buildTree(data)


    buildHuff(root, "")

    print(huff)

    encodedData = ""

    for char in data:
        encodedData += huff[char]

    return encodedData, root

def huffman_decoding(data,root):
    decoded = ""

    node = root

    for char in data:
        # print('Current char -> ' + char)
        
        if node.right is not None and char == '1':
            node = node.right
            if node.right is None and node.left is None:
                print('Reached leaf')
                decoded += node.symbol
                print('Decoding symbol -> ' + node.symbol)
                node = root
        if node.left is not None and char == '0':
            node = node.left
            if node.right is None and node.left is None:
                print('Reached leaf')
                decoded += node.symbol
                print('Decoding symbol -> ' + node.symbol)
                node = root
        
    print('Decoded -> ' + decoded)
    return decoded

if __name__ == "__main__":
    a_great_sentence = "AB"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    a_great_sentence1 = "The sky is blue"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence1)))
    print ("The content of the data is: {}\n".format(a_great_sentence1))

    encoded_data1, tree1 = huffman_encoding(a_great_sentence1)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data1, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data1))

    decoded_data1 = huffman_decoding(encoded_data1, tree1)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data1)))
    print ("The content of the encoded data is: {}\n".format(decoded_data1))

    a_great_sentence2 = "AABBCCDD"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence2)))
    print ("The content of the data is: {}\n".format(a_great_sentence2))

    encoded_data2, tree2 = huffman_encoding(a_great_sentence2)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data2, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data2))

    decoded_data2 = huffman_decoding(encoded_data2, tree2)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data2)))
    print ("The content of the encoded data is: {}\n".format(decoded_data2))