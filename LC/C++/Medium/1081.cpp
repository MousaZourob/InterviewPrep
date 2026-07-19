class Solution {
public:
    string smallestSubsequence(string s) {
        std::unordered_map<char, int> lastIndex{};
        for (int i = 0; i < s.size(); ++i ){
            lastIndex[s[i]] = i;
        }

        std::string ans{};
        std::unordered_set<char> seen{};
        for (int i = 0; i < s.size(); ++i) {
            char curr = s[i];
            if (!seen.contains(curr)) {
                while (!ans.empty() && curr < ans.back() && i < lastIndex[ans.back()]) {
                    seen.erase(ans.back());
                    ans.pop_back();
                }
                seen.insert(curr);
                ans.push_back(curr);
            }
        }

        return ans;
    }
};