class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = []
        curr = 1

        for i in range(n):
            ans.append(curr)
            print(curr)
            if curr * 10 <= n:
                curr *= 10
            else:
                while curr % 10 == 9 or curr >= n:
                    curr //= 10
                curr += 1
        
        return ans