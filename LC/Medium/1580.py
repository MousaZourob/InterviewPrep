class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        boxes.sort()
        ans = 0
        n = len(warehouse)
        l, r = 0, n - 1
        box_i = len(boxes)-1
        
        while l <= r and box_i >= 0:
            if boxes[box_i] <= warehouse[l]:
                l += 1
                ans += 1
            elif boxes[box_i] <= warehouse[r]:
                r -= 1
                ans += 1
            box_i -= 1
        
        return ans
                