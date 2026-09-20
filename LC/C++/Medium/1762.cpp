class Solution {
public:
    vector<int> findBuildings(vector<int>& heights) {
        int maxSeen = heights.back();
        std::vector<int> ans{};
        ans.push_back(heights.size() - 1);

        for (int i = heights.size() - 2; i >= 0; --i) {
            if (heights[i] > maxSeen) {
                ans.push_back(i);
                maxSeen = heights[i];
            }
        }
        
        for (int i = 0; i < ans.size() / 2; i++) {
            int temp = ans[i];
            ans[i] = ans[ans.size() - i - 1];
            ans[ans.size() - i - 1] = temp; 
        }
        return ans;
    }
};