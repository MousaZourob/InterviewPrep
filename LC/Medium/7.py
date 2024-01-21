class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2 ** 31 - 1

        remainder = abs(x)
        ans = 0

        while remainder > 0:
            remainder, digit = divmod(remainder, 10)

            digit_bound = INT_MAX % 10 if x > 0 else INT_MAX % 10 + 1

            if ans > INT_MAX // 10 or (ans == INT_MAX // 10 and digit > digit_bound):
                return 0

            ans = ans * 10 + digit

        return ans if x >= 0 else -ans