class Solution {
    int dfs(int curr, std::vector<int>& amounts) {
        int n = amounts.size();
        while (curr < n && amounts[curr] == 0) {
            curr += 1;
        }
        if (curr == n) {
            return 0;
        }

        int cost = std::numeric_limits<int>::max();

        for (int next = curr + 1; next < n; ++next) {
            if (amounts[next] * amounts[curr] < 0) {
                amounts[next] += amounts[curr];
                cost = std::min(cost, 1 + dfs(curr + 1, amounts));
                amounts[next] -= amounts[curr];
            }
        }

        return cost;
    }

public:
    int minTransfers(vector<vector<int>>& transactions) {
        std::unordered_map<int, int> balances{};
        for (auto& t : transactions) {
            balances[t[0]] -= t[2];
            balances[t[1]] += t[2];
        }

        std::vector<int> amts{};
        for (auto& [x, y] : balances) {
            if (y != 0) amts.push_back(y);
        }

        return dfs(0, amts);
    }
};