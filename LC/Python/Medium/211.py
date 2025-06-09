class Node:
    def __init__(self):
        self.is_word = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
            
        curr.is_word = True

    def search(self, word: str) -> bool:
        n = len(word)
        
        def dfs(curr, i):
            if i == n:
                return curr.is_word
            
            if word[i] == '.':
                for c in curr.children.values():
                    if dfs(c, i+1):
                        return True
            
            if word[i] in curr.children:
                return dfs(curr.children[word[i]], i + 1)
            
            return False
        
        return dfs(self.root, 0)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)