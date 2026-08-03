class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        std::unordered_map<int, int> freq{};
        for (int num : nums) freq[num]++;

        std::vector<std::vector<int>> buckets(nums.size() + 1);
        for (auto [x, count] : freq)
            buckets[count].push_back(x);

        std::vector<int> result;
        for (int count = nums.size(); count > 0 && result.size() < k; --count) {
            for (int x : buckets[count]) {
                result.push_back(x);
                if (result.size() == k) break;
            }
        }

        return result;
    }
};