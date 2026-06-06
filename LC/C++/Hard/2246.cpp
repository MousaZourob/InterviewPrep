class Solution {
    vector<vector<int>> adjList{};
    int ans;
public:
    int dfs(int i, string& s) {
        int best1 = 0, best2 = 0;
        for (int child : adjList[i]) {
            int childLen = dfs(child, s);
            if (s[child] == s[i]) continue;

            if (childLen > best1) { 
                best2 = best1; best1 = childLen; 
            } else if (childLen > best2) { 
                best2 = childLen; 
            }
        }
        ans = std::max(ans, 1 + best1 + best2);
        return 1 + best1;
    }

    int longestPath(vector<int>& parent, string s) {
        int n = parent.size();
        adjList.resize(n);
        for (size_t i{1}; i < n; ++i) {
            adjList[parent[i]].push_back(i);
        }
        dfs(0, s);
        return ans;
    }
};