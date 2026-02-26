class Solution {
    std::unordered_map<char, std::string> numLetters = {
        {'2', "abc"}, {'3', "def"}, {'4', "ghi"}, {'5', "jkl"},
        {'6', "mno"}, {'7', "pqrs"}, {'8', "tuv"}, {'9', "wxyz"}
    };

    std::vector<string> ans;
    std::string curr;
public:
    void dfs(int i, string& digits) {
        if (curr.size() == digits.size()) {
            ans.push_back(curr);
            return;
        }

        for (char& c : numLetters[digits[i]]) {
            curr.push_back(c);
            dfs(i + 1, digits);
            curr.pop_back();
        }
    }
    vector<string> letterCombinations(string digits) {
        ans.clear();
        curr.clear();

        if (!digits.empty()) {
            dfs(0, digits);
        }

        return ans;
    }
};