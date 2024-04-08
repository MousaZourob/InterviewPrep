class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = collections.Counter(students)
        n, i = len(students), 0
        
        while i < n and count[sandwiches[i]]:
            count[sandwiches[i]] -= 1
            i += 1
    
        return n - i