class UnionFind {
public:
    UnionFind(int n) : parent_(n), rank_(n, 0) {
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

    int unite(int a, int b) {
        a = find(a);
        b = find(b);

        if (a == b) return 0;

        parent_[b] = a;

        if (rank_[a] < rank_[b]) {
            std::swap(a, b);
        } else if (rank_[a] == rank_[b]) {
            rank_[a]++;
        }

        return 1;
    }

private:
    std::vector<int> parent_;
    std::vector<int> rank_;
};

class Solution {
public:
    int countComponents(int n, vector<vector<int>>& edges) {
        UnionFind uf(n);
        for (auto& edge : edges) {
            n -= uf.unite(edge[0], edge[1]);
        }

        return n;
    }
};