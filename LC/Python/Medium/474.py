class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        cache = {}

        def dfs(i, zeroes, ones):
            if (i, zeroes, ones) in cache:
                return cache[(i, zeroes, ones)]
            if i >= len(strs):
                return 0

            z_count = strs[i].count('0')
            o_count = len(strs[i]) - z_count
            taken = -1

            if (zeroes - z_count >= 0 and ones - o_count >= 0):
                taken = dfs(i + 1, zeroes - z_count, ones - o_count) + 1

            not_taken = dfs(i + 1, zeroes, ones)
            cache[(i, zeroes, ones)] = max(taken, not_taken)

            return cache[(i, zeroes, ones)]

        return dfs(0, m, n)