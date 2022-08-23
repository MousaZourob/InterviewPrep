from sortedcontainers import SortedList

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        window_start = 0
        curr_window = SortedList()
        n = 0
        ans = []
        
        for num in nums:
            curr_window.add(num)
            n += 1
            
            if n >= k:
                if k % 2 == 1:
                    ans.append(curr_window[k//2])
                else:
                    ans.append((curr_window[k//2 - 1] + curr_window[k//2])/2)
                
                curr_window.discard(nums[window_start])
                window_start += 1
        
        return ans