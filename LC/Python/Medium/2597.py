class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        n = len(nums)
        freq = defaultdict(int)
        
        def dfs(i):
            if i >= n:
                return 1
            
            res = dfs(i+1)
            if not freq[nums[i]+k] and not freq[nums[i]-k]:
                freq[nums[i]] += 1
                res += dfs(i+1)
                freq[nums[i]] -= 1
            return res
    
        return dfs(0) - 1