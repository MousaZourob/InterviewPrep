class Solution:
    def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:
        n = len(arrays)
        freqs = defaultdict(int)
        ans = []
        
        for array in arrays:
            for num in array:
                freqs[num] += 1
                if freqs[num] == n:
                    ans.append(num)
        
        return ans