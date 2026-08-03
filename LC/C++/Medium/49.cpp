class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::map<std::vector<int>, std::vector<string>> groups;

        for (const string& s : strs) {
            std::vector<int> chars(26);

            for (char c : s) {
                chars[c - 'a']++;
            }

            groups[chars].push_back(s);
        }

        vector<vector<string>> ans;
        for (auto& [key, group] : groups) {
            ans.push_back(move(group));
        }

        return ans;
    }
};