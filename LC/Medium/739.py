class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0]*n
        stack = []

        for curr_day in range(n):
            while stack and temperatures[stack[-1]] < temperatures[curr_day]:
                past_day = stack.pop()
                ans[past_day] = curr_day - past_day

            stack.append(curr_day)

        return ans