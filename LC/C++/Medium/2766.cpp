class Solution {
public:
    vector<int> relocateMarbles(vector<int>& nums, vector<int>& moveFrom, vector<int>& moveTo) {
        std::set<int> positions(nums.begin(), nums.end());

        for (int i = 0; i < moveFrom.size(); ++i) {
            positions.erase(moveFrom[i]);
            positions.insert(moveTo[i]);
        }

        return std::vector<int>(positions.begin(), positions.end());
    }
};