"""

Implement a MapSum class with insert, and sum methods.

For the method insert, you'll be given a pair of (string, integer). The string represents the key and the integer represents the value. If the key already existed, then the original key-value pair will be overridden to the new one.

For the method sum, you'll be given a string representing the prefix, and you need to return the sum of all the pairs' value whose key starts with the prefix.

Example 1:
Input: insert("apple", 3), Output: Null
Input: sum("ap"), Output: 3
Input: insert("app", 2), Output: Null
Input: sum("ap"), Output: 5

"""


class Node:
    def __init__(self, st, is_valid=False, value=0):
        self.value = st
        self.children = set()
        self.valid = is_valid
        self.sum = value

    def get_childern(self):
        return self.children

    def add_children(self, st, is_valid=False, value = 0):
        node = Node(st, is_valid)
        self.children.add(node)
        node.sum += value
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

    def insert(self, word: str, value: int) -> None:
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
                return False, 0
        return node.is_valid(), node.sum
    
    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.head
        for chr in prefix:
            check_child, child_node = node.is_child(chr)
            if check_child:
                node = child_node
            else:
                return False
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Trie()
        

    def insert(self, key: str, val: int) -> None:
        node = self.root.head
        for chr in key:
            check_child, child_node = node.is_child(chr)
            if check_child:
                node = child_node
                child_node.sum += val
            else:
                node = node.add_children(chr)
                node.sum += val
        node.set_valid()
        return
        

    def sum(self, prefix: str) -> int:
        is_valid, sum  = self.root.search(prefix)
        return sum
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)

"""
class TrieNode(object):
    __slots__ = 'children', 'score'
    def __init__(self):
        self.children = {}
        self.score = 0

class MapSum(object):
    def __init__(self):
        self.map = {}
        self.root = TrieNode()

    def insert(self, key, val):
        delta = val - self.map.get(key, 0)
        self.map[key] = val
        cur = self.root
        cur.score += delta
        for char in key:
            cur = cur.children.setdefault(char, TrieNode())
            cur.score += delta

    def sum(self, prefix):
        cur = self.root
        for char in prefix:
            if char not in cur.children:
                return 0
            cur = cur.children[char]
        return cur.score
"""
