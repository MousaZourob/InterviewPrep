class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        slen, tlen = len(stamp), len(target)
        ans = []
        s_cover = set()
        
        for i in range(slen):
            for j in range(slen-i):
                s_cover.add('?'*i + stamp[i:slen-j] + '?'*j)
        
        s = '?'*tlen
        
        while target != s:
            found = False
            
            for i in range(tlen-slen, -1, -1):
                if target[i: i+slen] in s_cover:
                    target = target[:i] + '?' * slen + target[i+slen:]  
                    ans.append(i)
                    found = True
            if not found: 
                return []
        
        return ans[::-1]