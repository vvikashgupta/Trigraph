"""
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.
"""





class Node:
    def __init__(self, value, is_valid=False, weight=0):
        self.value = value
        self.valid = is_valid
        self.weight = weight
        self.children = set()
    
    def addNode(self, value, is_valid=False, weight=0):
        node = Node(value, is_valid, weight)
        self.children.add(node)
        return node
    
    def is_child(self, value):
        for child in self.children:
            if value[-1] == '.':
                return True, child
            if value[-1] == child.value[-1]:
                return True, child
        return False, None
    
    def is_valid(self):
        return self.valid
    
    def set_valid(self):
        self.valid = True
    
    def get_weight(self, weight):
        self.weight = weight
        
class Trie:
    def __init__(self):
        self.head = Node(None)
        
    def insert(self,st):
        node = self.head
        for index in range(len(st)):
            chr = "".join(st[:index+1])
            check_child, child_node = node.is_child(chr)
            if check_child:
                node = child_node
            else:
                node = node.addNode(chr)
        node.set_valid()

    def search(self, st):
        node = self.head
        for index in range(len(st)):
            chr = "".join(st[:index+1])
            check_child, child_node = node.is_child(chr)
            if check_child:
                node = child_node
            else:
                return False
        return True
            
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node(None)
        
    def addWord(self, st: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.head
        for index in range(len(st)):
            chr = st[:index+1]
            check_child, child_node = node.is_child(chr)
            if check_child:
                node = child_node
            else:
                node = node.addNode(chr)
        node.set_valid()
        

    def search(self, st: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to     represent any one letter.
        """
        node = self.head
        for index in range(len(st)):
            chr = "".join(st[:index+1])
            check_child, child_node = node.is_child(chr)
            if check_child:
                node = child_node
            else:
                return False
        return node.is_valid()
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
