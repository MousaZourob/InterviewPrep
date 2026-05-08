class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        std::vector<int> ans;
        std::deque<int> dq;
        int windowStart = 0;

        for (int windowEnd = 0; windowEnd < nums.size(); ++windowEnd) {
            while (!dq.empty() && nums[dq.back()] < nums[windowEnd]) {
                dq.pop_back();
            }
            dq.push_back(windowEnd);

            if (windowStart > dq[0]) {
                dq.pop_front();
            }

            if (windowEnd + 1 >= k) {
                ans.push_back(nums[dq[0]]);
                windowStart += 1;
            }
        }
        
        return ans;
    }
};