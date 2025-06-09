class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)
        freq = set(count.values())
        
        return len(freq) == len(count)