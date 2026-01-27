class Solution {
public:
    vector<vector<int>> minimumAbsDifference(vector<int>& arr) {
        std::vector<std::vector<int>> ans{};
        int minDiff = std::numeric_limits<int>::max();

        std::sort(arr.begin(), arr.end());

        for (int i = 0; i < arr.size() - 1; ++i) {
            if (std::abs(arr[i + 1] - arr[i]) < minDiff) {
                ans = {{arr[i], arr[i+1]}};
                minDiff = std::abs(arr[i + 1] - arr[i]);
            } else if (std::abs(arr[i + 1] - arr[i]) == minDiff) {
                ans.push_back({arr[i], arr[i+1]});
            }
        }

        return ans;
    }
};