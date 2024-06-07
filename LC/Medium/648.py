class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary = set(dictionary)
        ans = []
        
        for word in sentence.split():
            found = False
            for i in range(len(word)):
                if word[:i] in dictionary:
                    ans.append(word[:i])
                    found = True
                    break

            if not found:
                ans.append(word)
        
        return " ".join(ans)