class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        waits = []
        curr_time = 0
        for arrival, wait_time in customers:
            curr_time = max(curr_time, arrival)
            curr_time += wait_time
            waits.append(curr_time - arrival)
            
        return sum(waits) / len(waits)