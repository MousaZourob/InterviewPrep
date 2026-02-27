class Solution {
    std::map<std::pair<int, int>, int> cache{};
public:
    int dfs(int i, vector<int>& coins, int target) {
        auto state = std::make_pair(i, target);
        if (cache.count(state)) {
            return cache[state];
        }
        if (target == 0) {
            return 0;
        }
        if (i >= coins.size() || target < 0) {
            return std::numeric_limits<int>::max();
        }

        int skip = dfs(i + 1, coins, target);
        int take = dfs(i, coins, target - coins[i]);

        if (take != std::numeric_limits<int>::max()) {
            take += 1;
        }

        int res = std::min(skip, take);
        cache[state] = res;
        return res;
    }

    int coinChange(vector<int>& coins, int amount) {
        int n = coins.size();
        
        int ans = dfs(0, coins, amount);
        if (ans == std::numeric_limits<int>::max()) {
            return -1;
        }
        return ans;
    }
};