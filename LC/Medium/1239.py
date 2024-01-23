class Solution:
    def maxLength(self, arr: List[str]) -> int:    
        opt_set = set()
        for word in arr:
            self.word_to_bitset(opt_set, word)

        opt_arr = list(opt_set)
        return self.dfs(opt_arr, 0, 0)
        
    def word_to_bitset(self, opt_arr: Set[int], word: str) -> None:        
        char_bitset = 0
        for c in word:            
            mask = 1 << ord(c) - 97
            if char_bitset & mask:
                return
            char_bitset += mask

        opt_arr.add(char_bitset + (len(word) << 26))
        
    def dfs(self, opt_arr: List[int], pos: int, res: int) -> int:        
        old_chars = res & ((1 << 26) - 1)
        old_len = res >> 26
        best = old_len
        
        for i in range(pos, len(opt_arr)):
            new_chars = opt_arr[i] & ((1 << 26) - 1)
            new_len = opt_arr[i] >> 26
            
            if new_chars & old_chars:
                continue
            
            new_res = new_chars + old_chars + (new_len + old_len << 26)
            best = max(best, self.dfs(opt_arr, i + 1, new_res))
        return best
        