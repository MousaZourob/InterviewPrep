class Solution(object):
    def findKthNumber(self, n, k):
        curr = 1
        k -= 1

        while k > 0:
            steps = self.count_steps(n, curr, curr+1)
            if steps <= k:
                curr += 1
                k -= steps
            else:
                curr *= 10
                k -= 1
    
        return curr
    
    def count_steps(self, n, left, right):
        steps = 0
        while left <= n:
            steps += min(n + 1, right) - left
            left *= 10
            right *= 10

        return steps