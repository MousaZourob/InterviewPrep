class Solution:
    def minMaxDifference(self, num: int) -> int:
        max_num = str(num)
        min_num = str(num)

        for c in max_num:
            if c != '9':
                max_num = max_num.replace(c, "9")
                break

        min_num = min_num.replace(min_num[0], "0")

        return int(max_num) - int(min_num)