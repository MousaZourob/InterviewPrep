class Solution {
    vector<vector<int>> cache;
    int endingMask;
public:
    int dfs(int node, int mask, vector<vector<int>>& graph) {
        if (cache[node][mask] != 0) {
            return cache[node][mask];
        }
        if ((mask & (mask - 1)) == 0) {
            return 0;
        }
        
        cache[node][mask] = std::numeric_limits<int>::max() - 1;
        for (int neigh : graph[node]) {
            if ((mask & (1 << neigh)) != 0) {
                int alreadyVisited = dfs(neigh, mask, graph);
                int notVisited = dfs(neigh, mask ^ (1 << node), graph);
                int best = min(alreadyVisited, notVisited);
                cache[node][mask] = min(cache[node][mask], 1 + best);
            }
        }

        return cache[node][mask];
    }
    int shortestPathLength(vector<vector<int>>& graph) {
        int n = graph.size();
        endingMask = (1 << n) - 1;
        cache = vector<vector<int>>(n, vector<int>(endingMask + 1));

        int best = std::numeric_limits<int>::max();
        for (int i = 0; i < n; ++i) {
            best = min(best, dfs(i, endingMask, graph));
        }

        return best;
    }
};