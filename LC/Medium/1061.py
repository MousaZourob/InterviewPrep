class Solution:
    def find(self, x):
        if x not in self.union_find:
            self.union_find[x] = x
            return x

        if x != self.union_find[x]:
            return self.find(self.union_find[x])
        return x 
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x > root_y:
            self.union_find[root_x] = root_y
        else:
            self.union_find[root_y] = root_x

    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        self.union_find = {}
        for i in range(len(s1)):
            self.union(s1[i], s2[i])

        ans = [""] * len(baseStr)
        for i in range(len(baseStr)):
            ans[i] = self.find(baseStr[i])

        return "".join(ans)