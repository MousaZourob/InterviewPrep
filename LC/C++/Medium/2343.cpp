class Solution {
public:
    vector<int> smallestTrimmedNumbers(vector<string>& nums, vector<vector<int>>& queries) {
        std::vector<int> ans{};
        int n = nums.size();
        for (auto& q : queries) {
            std::priority_queue<std::pair<std::string, int>, std::vector<std::pair<std::string, int>>, std::greater<std::pair<std::string, int>>> pq;
            for (int i = 0; i < n; ++i) {
                std::string trimmed = nums[i].substr(nums[i].size() - q[1]);
                pq.push({trimmed, i});
            }

            while (q[0] > 1) {
                pq.pop();
                q[0]--;
            }
            ans.push_back(pq.top().second);
        }

        return ans;
    }
};