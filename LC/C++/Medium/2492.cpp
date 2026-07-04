class UnionFind {
    std::vector<int> parent, rank;
public:
    UnionFind(int size) {
        parent.resize(size);
        rank.resize(size, 0);
        for (size_t i{}; i < size; ++i) {
            parent[i] = i;
        }
    }

    int find(int x) {
        while (parent[x] != x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return parent[x];
    }

    void unify(int a, int b) {
        a = find(a);
        b = find(b);

        if (rank[a] < rank[b]) {
            std::swap(a, b);
        }

        parent[b] = a;
        if (rank[a] == rank[b]) rank[a]++;
    }
};

class Solution {
public:
    int minScore(int n, vector<vector<int>>& roads) {
        UnionFind dsu(n + 1);
        int ans = std::numeric_limits<int>::max();

        for (auto& road : roads) {
            dsu.unify(road[0], road[1]);
        }

        for (auto& road : roads) {
            if (dsu.find(1) == dsu.find(road[0])) {
                ans = std::min(ans, road[2]);
            }
        }

        return ans;
    }
};