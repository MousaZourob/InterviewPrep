from collections import deque

class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        n = len(status)
        can_open = [status[i] == 1 for i in range(n)]
        have_box = [False] * n
        seen = [False] * n

        ans = 0
        q = deque()

        for box in initialBoxes:
            have_box[box] = True
            if can_open[box]:
                q.append(box)
                seen[box] = True
                ans += candies[box]

        while q:
            curr_box = q.popleft()
            for key in keys[curr_box]:
                can_open[key] = True
                if not seen[key] and have_box[key]:
                    ans += candies[key]

                    q.append(key)
                    seen[key] = True
        
            for box in containedBoxes[curr_box]:
                have_box[box] = True
                if not seen[box] and can_open[box]:
                    ans += candies[box]

                    q.append(box)
                    seen[box] = True
    
        return ans