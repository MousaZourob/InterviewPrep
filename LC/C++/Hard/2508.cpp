class Solution {
public:
    bool isPossible(int n, vector<vector<int>>& edges) {
        vector<int> degree(n + 1, 0);
        std::set<vector<int>> edgeSet{};

        for (auto& e : edges) {
            degree[e[0]]++;
            degree[e[1]]++;
            edgeSet.insert({min(e[0], e[1]), max(e[0], e[1])});
        }

        auto hasEdge = [&](int u, int v) {
            return edgeSet.count({min(u,v), max(u,v)});
        };

        vector<int> oddNodes{};
        for (size_t i{1}; i <= n; ++i) {
            if (degree[i] % 2 == 1) oddNodes.push_back(i);
        }

        if (oddNodes.size() == 0) return true;

        if (oddNodes.size() == 2) {
            int a = oddNodes[0];
            int b = oddNodes[1];

            if (!hasEdge(a, b)) return true;

            for (size_t k{1}; k <= n; ++k) {
                if (k == a || k == b) return false;
                if (!hasEdge(a, k) && !hasEdge(k, b)) return true;
            }
            return false;
        }

        if (oddNodes.size() == 4) {
            int a = oddNodes[0];
            int b = oddNodes[1];
            int c = oddNodes[2];
            int d = oddNodes[3];

            if (!hasEdge(a, b) && !hasEdge(c, d)) return true;
            if (!hasEdge(a, c) && !hasEdge(b, d)) return true;
            if (!hasEdge(a, d) && !hasEdge(b, c)) return true;
        }

        return false;
    }
};