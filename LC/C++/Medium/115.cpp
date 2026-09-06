class Solution {
    size_t m;
    size_t n;
    std::vector<std::vector<int>> cache_;
public:
    int dfs(string& s, string& t, size_t i, size_t j) {
        if (j == n) return 1;
        if (i == m) return 0;
        if (cache_[i][j] != -1) return cache_[i][j];
        if ((m - i) < (n - j)) return 0;

        int res = dfs(s, t, i + 1, j);
        if (s[i] == t[j]) res += dfs(s, t, i + 1, j + 1);

        return cache_[i][j] = res;
    }

    int numDistinct(string& s, string& t) {
        m = s.size();
        n = t.size();
        cache_.resize(m, std::vector(n, -1));

        return dfs(s, t, 0, 0);
    }
};