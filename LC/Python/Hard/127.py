class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return 0
        n = len(beginWord)
        
        word_hash = defaultdict(list)
        for word in wordList:
            for j in range(n):
                pattern = word[:j] + "*" + word[j + 1:]
                word_hash[pattern].append(word)
            
        visited = {}
        q = [(beginWord, 1)]
        
        while q:
            word, level = q.pop(0)
            visited[word] = True
           
            for i in range(n):
                pattern = word[:i] + "*" + word[i + 1:]
                for nextWord in word_hash[pattern]:
                    if nextWord == endWord:
                        return level + 1
                    if nextWord not in visited:
                        q.append((nextWord, level + 1))
                word_hash[pattern] = []
                
        return 0           