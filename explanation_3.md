# Huffman Coding

To implement the Huffman coding algorithm I decided to choose a binary tree as the optimal data structure. After building the frequency dictionary (which uses an ordered dictionary structure), the binary tree is built using the `buildTree()` method. It removes the first two elements from the frequency dictionary, creates two leaf `Node` objects, which contain these two symbols and their frequencies, and a sum node which references both these leaf nodes and also stores the total frequency of the symbols. It then continues to remove two nodes at a time from the frequency dictionary (if possible). When there are two nodes left, the root is created. After that, the `buildHuff()` method builds the Huffman dictionary which contains the letters in the original sentence and their corresponding encoded value.

- The `huffman_encoding()` method has a space complexity of O(n) because it has to traverse the entire original sentence to build out the tree and the Huffman dictionary and a time complexity of O(n*log(n)) because of the `sortDict()` method
- The `huffman_decoding()` method has a time and space complexity of O(n) because it traverses the encoded sentence
