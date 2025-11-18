class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        curr = k

        for n in nums:
            if n == 1:
                if curr < k:
                    return False
                curr = 0
            else:
                curr += 1

        return True
