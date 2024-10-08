class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m*n:
            return []

        ans = []
        for i in range(m):
            curr = []            
            for j in range(n):
                curr.append(original[i*n + j])
            ans.append(curr)

        return ans