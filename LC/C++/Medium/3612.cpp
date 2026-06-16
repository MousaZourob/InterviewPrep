class Solution {
public:
    string processStr(string s) {
        std::string ans{};

        for (char& c : s) {
            if (c == '*') {
                if (!ans.empty()) {
                    ans.pop_back();
                }
            } else if (c == '#') {
                ans += ans;
            } else if (c == '%') {
                std::ranges::reverse(ans);
            } else {
                ans += c;
            }
        }

        return ans;
    }
};