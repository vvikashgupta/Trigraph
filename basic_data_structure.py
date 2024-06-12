class Node:
    def __init__(self, st, is_valid=False):
        self.value = st
        self.children = set()
        self.valid = is_valid
        
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
