class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_last = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        root = self.root

        for ch in word:
            if ch not in root.children:
                root.children[ch] = TrieNode()
            root = root.children[ch]

        root.is_last = True


    def search(self, word: str) -> bool:
        if not word:
            return False

        root = self.root

        for ch in word:
            if ch not in root.children:
                return False
            root = root.children[ch]

        return root.is_last == True
        

    def startsWith(self, prefix: str) -> bool:
        if not prefix:
            return False

        root = self.root

        for ch in prefix:
            if ch not in root.children:
                return False
            root = root.children[ch]

        return True

        
        