class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        n = len(items)
        items.sort(key = lambda x: x[0])
        prefix = [0]
        
        max_beauty = 0
        for price, beauty in items:
            max_beauty = max(max_beauty, beauty)
            prefix.append(max_beauty)
        
        prices = [i[0] for i in items]
        ans = []
        
        for q in queries:
            i = bisect_right(prices, q)
            ans.append(prefix[i])
            
        return ans