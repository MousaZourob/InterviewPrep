class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        
        ans = [folder[0]]
        
        for f in folder[1:]:
            last_folder = ans[-1]
            last_folder += '/'
            if not f.startswith(last_folder):
                ans.append(f)
        
        return ans