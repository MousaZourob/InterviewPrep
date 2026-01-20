#include <array>
#include <vector>

class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        const int n = temperatures.size();
        std::vector<std::pair<int, int>> stack;
        std::vector<int> ans(n, 0);

        for (int i = 0; i < n; ++i) {
            while (!stack.empty() and stack.back().second < temperatures[i]) {
                auto [j, temp] = stack.back();
                stack.pop_back();
                ans[j] = i - j;
            }
            stack.emplace_back(std::make_pair(i, temperatures[i]));
        }

        return ans;
    }
};