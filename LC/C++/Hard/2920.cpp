class Solution {
    std::vector<std::vector<int>> cache_{};
    int dfs(std::vector<std::vector<int>>& adjList, std::vector<int>& coins, int k, int i, int parent, int h) {
        if (cache_[i][h] != INT_MIN) return cache_[i][h];
        
        long long currVal = coins[i] / (1 << h);

        long long opt1 = currVal - k;
        long long opt2 = currVal >> 1;

        for (auto child : adjList[i]) {
            if (child != parent) {
                opt1 += dfs(adjList, coins, k, child, i, h);
                if (h + 1 < 14) opt2 += dfs(adjList, coins, k, child, i, h + 1);
            }
        }

        return cache_[i][h] = std::max(opt1, opt2);
    }

public:
    int maximumPoints(vector<vector<int>>& edges, vector<int>& coins, int k) {
        int n = edges.size();
        cache_.assign(n + 1, std::vector<int>(15, INT_MIN));

        std::vector<std::vector<int>> adjList(n + 1);
        for (auto& edge : edges) {
            int a = edge[0];
            int b = edge[1];
            adjList[a].push_back(b);
            adjList[b].push_back(a);
        }

        return dfs(adjList, coins, k, 0, -1, 0);
    }
};