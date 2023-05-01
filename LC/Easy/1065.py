class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        
        node.is_word = True
    
class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        trie = Trie()
        
        for word in words:
            trie.insert(word)
            
        ans = []
        
        for i in range(len(text)):
            node = trie.root
            for j in range(i, len(text)):
                if text[j] not in node.children:
                    break
                node = node.children[text[j]]
                if node.is_word:
                    ans.append([i, j])
        
        return ans