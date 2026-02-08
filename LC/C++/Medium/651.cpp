class Solution {
public:
    std::unordered_map<int, int> cache{};

    int dfs(int n) {
        if (n <= 5) {
            return n;
        }

        if (cache.count(n)) {
            return cache[n];
        }

        int ans = n;
        for (int i = 3; i <= 6; ++i) {
            ans = max(ans, i * dfs(n - i - 1));
        }
        cache[n] = ans;
        return ans;
    }

    int maxA(int n) {
        return dfs(n);
    }
};