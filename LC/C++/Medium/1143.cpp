class Solution {
    std::vector<std::vector<int>> cache_;

    int dfs(int i, int j, const string& text1, const string& text2) {
        int m = text1.size();
        int n = text2.size();

        if (i == m || j == n)
            return 0;

        if (cache_[i][j] != -1)
            return cache_[i][j];

        int res = 0;
        if (text1[i] == text2[j]) {
            res = 1 + dfs(i + 1, j + 1, text1, text2);
        } else {
            res = max(
                dfs(i + 1, j, text1, text2),
                dfs(i, j + 1, text1, text2)
            );
        }

        return cache_[i][j] = res;
    }

public:
    int longestCommonSubsequence(string text1, string text2) {
        int m = text1.size();
        int n = text2.size();

        cache_.resize(m, std::vector<int>(n, -1));

        int ans = 0;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (text1[i] == text2[j]) {
                    ans = std::max(ans, 1 + dfs(i + 1, j + 1, text1, text2));
                }
            }
        }

        return ans;
    }
};