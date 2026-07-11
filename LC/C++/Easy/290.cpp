class Solution {
public:
    bool wordPattern(string pattern, string s) {
        std::istringstream iss(s);
        std::vector<std::string> words{
            std::istream_iterator<std::string>(iss),
            std::istream_iterator<std::string>()
        };

        if (pattern.size() != words.size()) {
            return false;
        }

        std::unordered_map<char, std::string> mapping{};
        std::unordered_set<std::string> mapped{};
        for (size_t i{}; i < pattern.size(); ++i) {
            char curr = pattern[i];
            if (!mapping.contains(curr)) {
                mapping[curr] = words[i];
                if (mapped.contains(words[i])) return false;
                mapped.insert(words[i]);
            }

            if (mapping[curr] != words[i]) {
                return false;
            }
        }

        return true;
    }
};