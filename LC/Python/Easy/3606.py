class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        def is_valid(s):
            return bool(re.fullmatch(r'[A-Za-z0-9_]+', s))

        order = {
            "electronics": 0,
            "grocery": 1,
            "pharmacy": 2,
            "restaurant": 3
        }

        ans = []

        for i in range(len(code)):
            if is_valid(code[i]) and businessLine[i] in order and isActive[i]:
                ans.append((order[businessLine[i]], code[i]))

        ans.sort()
        return [c for _, c in ans]
