class UnionFind {
public:
    UnionFind(int n) : parent_(n), rank_(n, 1) {
        for (size_t i{}; i < n; ++i) {
            parent_[i] = i;
        }
    }

    int find(int x) {
        while (x != parent_[x]) {
            parent_[x] = parent_[parent_[x]];
            x = parent_[x];
        }

        return x;
    }

    void unite(int a, int b) {
        a = find(a);
        b = find(b);

        if (a == b) return;


        if (rank_[a] > rank_[b]) {
            std::swap(a, b);
        } 
        
        parent_[b] = a;
        rank_[a] += rank_[b];

        return;
    }
    std::vector<int> parent_;
    std::vector<int> rank_;
};

class Solution {
public:
    int countCompleteComponents(int n, vector<vector<int>>& edges) {
        UnionFind uf(n);
        for (auto& edge : edges) {
            uf.unite(edge[0], edge[1]);
        }

        std::unordered_map<int, int> edgeCount{};
        for (auto& edge : edges) {
            int root = uf.find(edge[0]);
            edgeCount[root]++;
        }

        int ans = 0;
        for (size_t i{}; i < n; ++i) {
            if (uf.parent_[i] == i) {
                int nodeCount = uf.rank_[i];
                int expectedEdges = (nodeCount * (nodeCount - 1)) / 2;
                if (edgeCount[i] == expectedEdges) {
                    ans++;
                }
            }
        }

        return ans;
    }
};