class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path = set()
        ROW, COL = len(board), len(board[0])
        
        word_dict = Counter(word)
        board_dict = Counter(itertools.chain.from_iterable(board))

        if any (count > board_dict[char] for char, count in word_dict.items()):
            return False

        if board_dict[word[0]] > board_dict[word[-1]]:
            word = word[::-1]
        
        def dfs(r, c, i):
            if i == len(word):
                return True
            
            if r < 0 or r >= ROW:
                return False
            if c < 0 or c >= COL:
                return False
            if word[i] != board[r][c] or (r,c) in path:
                return False
            
            path.add((r,c))
            
            ans = (dfs(r+1, c, i+1) or 
                   dfs(r-1, c, i+1) or 
                   dfs(r, c+1, i+1) or
                   dfs(r, c-1, i+1))
            
            path.remove((r,c))
            
            return ans
        
        for r in range(ROW):
            for c in range(COL):
                if dfs(r, c, 0):
                    return True
        
        return False