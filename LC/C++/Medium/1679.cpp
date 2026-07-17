class Solution {
public:
    int maxOperations(vector<int>& nums, int k) {
        std::unordered_map<int, int> count{};

        int ans = 0;
        for (int num : nums) {
            int diff = k - num;
            if (count.contains(diff)) {
                count[diff]--;
                if (count[diff] == 0) count.erase(diff);
                ans++;
            } else {
                count[num]++;
            }
        }

        return ans;
    }
};