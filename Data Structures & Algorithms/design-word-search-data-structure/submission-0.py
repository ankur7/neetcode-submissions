
class TrieNode:
    def __init__(self):
        self.child = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        root = self.root
        
        for ch in word:
            if ch not in root.child:
                root.child[ch] = TrieNode()
                
            root = root.child[ch]

        root.is_end = True
        print(self.root)

        

    def search(self, word: str) -> bool:

        def dfs(j, root):
            cur = root
            
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for _, child in cur.child.items():
                        if dfs(i + 1, child):
                            return True
                    return False

                else:
                    if c not in cur.child:
                        return False
                    cur = cur.child[c]
            return cur.is_end


        return dfs(0, self.root)


        
        
