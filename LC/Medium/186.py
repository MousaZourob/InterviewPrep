class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse ()
        start = 0
        
        for stop in range(len(s) + 1):
            if stop == len(s) or s[stop] == " ":
                l, r = start, stop - 1
                while l < r:
                    s[l], s[r] = s[r], s[l]
                    l += 1
                    r -= 1
                start = stop + 1
                
            