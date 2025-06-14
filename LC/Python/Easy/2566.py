class Solution:
    def minMaxDifference(self, num: int) -> int:
        max_num = str(num)
        min_num = str(num)

        for c in max_num:
            if c != '9':
                max_num = max_num.replace(c, "9")
                break
        for c in min_num:
            if c != '0':
                min_num = min_num.replace(c, "0")
                break
        return int(max_num) - int(min_num)