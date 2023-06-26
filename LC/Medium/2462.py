class Solution:
    def totalCost(self, costs: List[int], k: int, m: int) -> int:
        n = len(costs)
        if n == k:
            return sum(costs)
        ans = 0
        heap = []
        
        left = costs[:m]
        right = costs[max(len(costs) - m, m):]
        heapify(left)
        heapify(right)
        l, r = m, max(len(costs) - m, m) - 1
        
        for _ in range(k):
            if left and right:
                if left[0] <= right[0]:
                    ans += heappop(left)
                    
                    if l <= r:
                        heappush(left, costs[l])
                        l += 1
                else:
                    ans += heappop(right)
                    
                    if l <= r:
                        heappush(right, costs[r])
                        r -= 1
            elif left:
                ans += heappop(left)
            else:
                ans += heappop(right)
            
        return ans