class Solution {
    std::vector<char> stack_;
    std::vector<string> ans_;
    
    void dfs(int n, int l, int r) {
        if (l == n && r == n) {
            ans_.emplace_back(stack_.begin(), stack_.end());
            return;
        }

        if (l == n) {
            stack_.push_back(')');
            dfs(n, l, r + 1);
            stack_.pop_back();
        } else if (l == r) {
            stack_.push_back('(');
            dfs(n, l + 1, r);
            stack_.pop_back();
        } else {
            stack_.push_back('(');
            dfs(n, l + 1, r);
            stack_.pop_back();

            stack_.push_back(')');
            dfs(n, l, r + 1);
            stack_.pop_back();
        }
    }

public:
    vector<string> generateParenthesis(int n) {
        dfs(n, 0, 0);
        return ans_;
    }
};