class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        arr_count = Counter(arr).most_common()
        length = len(arr)
        target = length // 2
        ans = 0
        
        for p in arr_count:
            length -= p[1]
            ans += 1
            if length <= target:
                break
        
        return ans