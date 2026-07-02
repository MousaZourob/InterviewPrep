class ValidWordAbbr {
    std::unordered_map<std::string, std::string> words;
    std::string abbr(const std::string& word) {
        if (word.size() <= 2) return word;
        return word.front() + std::to_string(word.size() - 2) + word.back();
    }

public:
    ValidWordAbbr(vector<string>& dictionary) {
        for (auto& word : dictionary) {
            auto abr = abbr(word);
            if (!words.contains(abr)) words[abr] = word;
            else if (words[abr] != word) words[abr] = "";
        }
    }
    
    bool isUnique(string word) {
        auto abr = abbr(word);
        return !words.contains(abr) || words[abr] == word;
    }
};

/**
 * Your ValidWordAbbr object will be instantiated and called as such:
 * ValidWordAbbr* obj = new ValidWordAbbr(dictionary);
 * bool param_1 = obj->isUnique(word);
 */