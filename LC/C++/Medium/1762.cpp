class Solution {
public:
    vector<int> findBuildings(vector<int>& heights) {
        int maxSeen = heights.back();
        std::vector<int> ans{};
        ans.push_back(heights.size() - 1);

        for (int i = heights.size() - 2; i >= 0; --i) {
            if (heights[i] > maxSeen) {
                ans.push_back(i);
            }
            maxSeen = std::max(maxSeen, heights[i]);
        }
        
        std::reverse(ans.begin(), ans.end());
        return ans;
    }
};