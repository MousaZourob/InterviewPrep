class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        vowels = set(vowels)
        
        count = defaultdict(int)
        for c in s:
            if c in vowels:
                count[c] += 1
                
        sortedVowel = "AEIOUaeiou"
        ans = []
        j = 0
        for c in s:
            if c not in vowels:
                ans.append(c)
            else:
                while count[sortedVowel[j]] == 0:
                    j += 1

                ans.append(sortedVowel[j])
                count[sortedVowel[j]] -= 1

        return ''.join(ans)