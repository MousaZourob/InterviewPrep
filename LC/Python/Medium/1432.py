class Solution:
    def maxDiff(self, num: int) -> int:
        max_num = str(num)

        for c in max_num:
            if c != "9":
                max_num = max_num.replace(c, "9")
                break

        min_num = str(num)
        if min_num[0] != "1":
            min_num = min_num.replace(min_num[0], "1")
        else:
            for c in min_num[1:]:
                if c != "1" and c != "0":
                    min_num = min_num.replace(c, "0")
                    break
        return int(max_num) - int(min_num)
