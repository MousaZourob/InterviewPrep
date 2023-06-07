class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        min_n = min(arr)
        max_n = max(arr)
        n = len(arr)
        gap = (max_n - min_n) / (n - 1)
        if gap == 0: return True
        s = set(num - min_n for num in arr)
        return len(s) == len(arr) and all(diff % gap == 0 for diff in s)