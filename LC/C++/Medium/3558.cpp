class Solution {
public:
    int assignEdgeWeights(vector<vector<int>>& edges) {
        const int MOD = 1e9 + 7;
        int n = edges.size() + 1;
        std::vector<std::vector<int>> adjList(n + 1);

        for (auto& e : edges) {
            adjList[e[0]].push_back(e[1]);
            adjList[e[1]].push_back(e[0]);
        }

        vector<bool> visited(n + 1, false);
        queue<pair<int,int>> q;
        q.push({1, 0});
        visited[1] = true;
        int maxDepth = 0;
        while (!q.empty()) {
            auto [node, depth] = q.front(); q.pop();
            maxDepth = max(maxDepth, depth);
            for (int neighbor : adjList[node]) {
                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    q.push({neighbor, depth + 1});
                }
            }
        }
        long long res = 1, base = 2;
        int exp = maxDepth - 1;
        while (exp > 0) {
            if (exp & 1) res = res * base % MOD;
            base = base * base % MOD;
            exp >>= 1;
        }
        return (int)res;
    }
};