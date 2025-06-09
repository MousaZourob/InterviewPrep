class Solution:
    def longestCommonPrefix(self, arr1, arr2):
        prefixes = set()
        ans = 0
        
        for num in arr1:
            while num not in prefixes and num > 0:
                prefixes.add(num)
                num //= 10

        for num in arr2:
            while num not in prefixes and num > 0:
                num //= 10
            if num > 0:
                ans = max(ans, len(str(num)))

        return ans