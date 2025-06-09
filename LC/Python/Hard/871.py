class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        missed_stations = []
        ans = 0
        prev = 0
        stations.append([target, 0])
        
        for distance, gas in stations:
            startFuel -= distance - prev
            
            while missed_stations and startFuel < 0:
                startFuel += -heapq.heappop(missed_stations)
                ans += 1
                
            if startFuel < 0: 
                return -1
            
            heapq.heappush(missed_stations, -gas)
            prev = distance

        return ans