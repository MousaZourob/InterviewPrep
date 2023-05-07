class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded = []
        
        for word in strs:
            encoded.append(f"{len(word)}${word}")
        
        return "".join(encoded)
        
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        ans = []
        i = 0
        
        while i < len(s):
            j = i
            while j < len(s) and s[j] != "$":
                j += 1
            curr_len = int(s[i:j])
            
            ans.append(s[j+1: j + 1 + curr_len])
            i = j + 1 + curr_len
        
        return ans
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))