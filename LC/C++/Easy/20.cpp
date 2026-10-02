class Solution {
public:
    bool isValid(string s) {
        std::stack<char> stack_;
        std::unordered_map<char, char> mapping{
            {')', '('},
            {'}', '{'},
            {']', '['}
        };

        for (auto& c : s) {
            if (mapping.contains(c)) {
                if (stack_.empty()) return false;
                char top = stack_.top();
                
                if (top != mapping[c]) return false;
                stack_.pop();
            } else {
                stack_.push(c);
            }
        }

        return stack_.empty();
    }
};