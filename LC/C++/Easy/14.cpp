class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        for (size_t i{}; i < strs[0].size(); ++i) {
            char c = strs[0][i];
            for (size_t j{1}; j < strs.size(); ++j) {
                if (i >= strs[j].size() || strs[j][i] != c) {
                    return strs[0].substr(0, i);
                }
            }
        }

        return strs[0];
    }
};