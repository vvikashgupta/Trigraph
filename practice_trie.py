#import sys,os


class Node():
    def __init__(self, st, isValid=False):
        self.st = st
        self.isValid = isValid
        self.children = set()
        self.word = None

    def is_valid(self):
        return True if self.isValid else False

    def set_valid(self):
        self.isValid = True

    def get_children(self):
        return self.children

    def add_child(self, st):
        node = Node(st)
        self.children.add(node)
        return node

    def is_child(self, st):
        for child in self.children:
            if child.st == st:
                return True, child
        return False, None

    def get_value(self):
        return self.st

class Trie():
    def __init__(self):
        self.head = Node(None)

    def insert(self, word):
        node = self.head
        for ch in word:
            status,child = node.is_child(ch)
            if status:
                node = child
            else:
                node = node.add_child(ch)
        node.word = word
        node.set_valid()

    def search(self, word):
        node = self.head
        for ch in word:
            status, child = node.is_child(ch)
            if status:
                node = child
            else:
                return False, False
        return node.is_valid() 

    def startswith(self, word):
        node = self.head
        for ch in word:
            status, child = node.is_child(ch)
            if status:
                node = child
            else:
                return False
        return True, node

    def printme(self,node):
        nodes = node.get_children()
        if not nodes:
            return
        else:
            for node in nodes:
                print(node.get_value())
                if node.word:
                    print(node.word)
                self.printme(node)
            return 
 
    def get_follower(self, node, result = []):
        nodes = node.get_children()
        if not nodes:
            return
        else:
            for node in nodes:
                #print(node.get_value())
                if node.word:
                    print(node.word)
                    result.append(node.word)
                self.get_follower(node,result)
            return 
                 

def main():
    graph = Trie()
    suggestions = []
    wordlist = ['hello', 'my' , 'mame' , 'is', 'icks' ]
    print(wordlist)
    searchlist = ['i', 'm']
    for word in wordlist:
        graph.insert(word)
    graph.printme(graph.head)
    result_set = []
    for item in searchlist:
        status, node = graph.startswith(item)
        if status: result_set.append(node)
    for node in result_set:
        graph.get_follower(node, suggestions)
    print(suggestions)
         
    
        
    


if __name__ == '__main__':
    main()
