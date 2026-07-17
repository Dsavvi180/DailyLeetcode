import string
class TrieNode:
    def __init__(self, isEnd=False):
        self.children = {x: None for x in string.ascii_lowercase}
        self.isEnd = isEnd
        

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for i in range(len(word)):
            char = word[i]
            if not node.children[char]:
                node.children[char] = TrieNode()
            node = node.children.get(char)
            if i == len(word) -1:
                node.isEnd = True

    def search(self, word: str) -> bool:
        node = self.root
        for i in range(len(word)):
            char = word[i]
            node = node.children.get(char)
            if not node: return False
            if i == len(word)-1 and node.isEnd: return True
        return False


    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for i in range(len(prefix)):
            char = prefix[i]
            node = node.children.get(char)
            if not node: return False
        return True
        
        
        