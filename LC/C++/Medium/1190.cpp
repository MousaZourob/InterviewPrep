class Solution {
public:
    string reverseParentheses(string s) {
        std::stack<int> stack_;
        std::string ans{};

        for (auto& c : s) {
            if (c == '(') {
                stack_.push(ans.size());
            } else if (c == ')') {
                std::reverse(ans.begin() + stack_.top(), ans.end());
                stack_.pop();
            } else {
                ans += c;
            }
        }

        return ans;
    }
};