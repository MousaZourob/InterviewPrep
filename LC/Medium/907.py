class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 0
        stack = []
        
        for i in range(n+1):
            while stack and (i == n or arr[stack[-1]] >= arr[i]):
                mid = stack.pop()
                left = -1 if not stack else stack[-1]
                right = i
                
                count = (mid - left) * (right - mid)
                ans += (count * arr[mid])

            stack.append(i)
        
        return ans % (10**9 + 7)