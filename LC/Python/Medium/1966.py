class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x:(-x[0],x[1]))
        max_defence = 0
        ans = 0
        
        for attack, defence in properties:
            if max_defence > defence:
                ans += 1
            else:
                max_defence = defence
        
        return ans
        