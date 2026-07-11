class Solution {
    std::unordered_map<char, std::string> charToWord{};
    std::unordered_set<string> usedWords{};

    bool backtrack(std::string& pattern, int i, std::string& s, int j) {
        if (i == pattern.size() && j == s.size()) return true;
        if (i == pattern.size() || j == s.size()) return false;

        char c = pattern[i];

        if (charToWord.contains(c)) {
            std::string& mapped = charToWord[c];

            if (s.compare(j, mapped.size(), mapped) != 0) return false;
            return backtrack(pattern, i + 1, s, j + mapped.size());
        }

        for (size_t len{1}; j + len <= s.size(); ++len) {
            string candidate = s.substr(j, len);

            if (usedWords.count(candidate)) continue;

            charToWord[c] = candidate;
            usedWords.insert(candidate);

            if (backtrack(pattern, i + 1, s, j + len)) return true;

            charToWord.erase(c);
            usedWords.erase(candidate);
        }

        return false;
    }

public:
    bool wordPatternMatch(string pattern, string s) {
        return backtrack(pattern, 0, s, 0);
    }
};