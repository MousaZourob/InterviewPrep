class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, x):
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x
    
    def union(self, x1, x2):
        p1, p2 = self.find(x1), self.find(x2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        email_to_acc = {}
        
        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e in email_to_acc:
                    uf.union(i, email_to_acc[e])
                else:
                    email_to_acc[e] = i
                
        email_group = defaultdict(list)
        for e, i in email_to_acc.items():
            leader = uf.find(i)
            email_group[leader].append(e)
            
        ans = []
        for i, emails in email_group.items():
            name = accounts[i][0]
            ans.append([name] + sorted(email_group[i]))
        
        return ans