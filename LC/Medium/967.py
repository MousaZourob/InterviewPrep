class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        ans = []
        q = [(1, d) for d in range(1, 10)]
        
        while q:
            p, curr_num = q.pop()
            
            if p == n:
                ans.append(curr_num)
            else:
                for j in range(10):
                    if abs(curr_num % 10 - j) == k: 
                        q.append((p + 1, curr_num * 10 + j))
        
        return ans