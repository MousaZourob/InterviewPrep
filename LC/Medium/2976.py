class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        distance_matrix = [[inf] * 26 for _ in range(26)]
        
        for start, end, weight in zip(original, changed, cost):
            start_c = ord(start) - ord('a')
            end_c = ord(end) - ord('a')

            distance_matrix[start_c][end_c] = min(distance_matrix[start_c][end_c], weight)

        for k in range(26):
            for i in range(26):
                for j in range(26):
                    distance_matrix[i][j] = min(distance_matrix[i][j], distance_matrix[i][k] + distance_matrix[k][j])
        
        ans = 0
        
        for start, end in zip(source, target):
            if start == end:
                continue
            
            start_c = ord(start) - ord('a')
            end_c = ord(end) - ord('a')
            
            if distance_matrix[start_c][end_c] == inf:
                return -1
            ans += distance_matrix[start_c][end_c]
        
        return ans