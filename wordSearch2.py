'''
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

Example:

Input: 
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]
 

Note:

All inputs are consist of lowercase letters a-z.
The values of words are distinct.
'''






class Node:
    def __init__(self, st, is_valid=False):
        self.value = st
        self.children = set()
        self.valid = is_valid
        self.word = None

    def get_childern(self):
        return self.children

    def add_children(self, st, is_valid=False):
        node = Node(st, is_valid)
        self.children.add(node)
        return node


    def is_child(self, chr):
        for child in self.children:
            if child.value == chr:
                return True, child
        return False, None

    def is_valid(self):
        return self.valid

    def set_valid(self):
        self.valid = True
        
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node(None, True)

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.head
        insert_flag = False
        str_len = len(word)
        for index, chr in enumerate(word):
            check_child, child_node = node.is_child(chr)
            if check_child:
                node = child_node
            else:
                node = node.add_children(chr)
        node.set_valid()
        node.word = word

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.head
        for chr in word:
            check_child, child_node = node.is_child(chr)
            if check_child:
                node = child_node
            else:
                return False
        return node.is_valid()

        
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        result = []
        for row in board:
            for col in range(len(board[0])):
