class Solution {
    std::vector<bool> visited;

    void dfs(int curr, vector<vector<int>>& isConnected) {
        visited[curr] = true;

        for (int nei = 0; nei < isConnected.size(); ++nei) {
            if (isConnected[curr][nei] && !visited[nei]) {
                dfs(nei, isConnected);
            }
        }
    }

public:
    int findCircleNum(vector<vector<int>>& isConnected) {
        int n = isConnected.size();
        visited.assign(n, false);
        int ans = 0;

        for (int i = 0; i < n; ++i) {
            if (!visited[i]) {
                dfs(i, isConnected);
                ++ans;
            }
        }

        return ans;
    }
};