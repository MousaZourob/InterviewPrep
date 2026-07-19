class Solution {
    std::vector<std::string> ans{};

public:
    void dfs(const std::string& word, int i, int count, std::string curr) {
        if (i == word.size()) {
            if (count > 0) curr += std::to_string(count);
            ans.push_back(curr);
            return;
        }

        dfs(word, i + 1, count + 1, curr);

        std::string next = curr;
        if (count > 0) next += std::to_string(count);
        next += word[i];
        dfs(word, i + 1, 0, next);

        return;
    }

    vector<string> generateAbbreviations(string word) {
        dfs(word, 0, 0, "");
        return ans;
    }
};