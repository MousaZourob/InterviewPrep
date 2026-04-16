class WordDistance {
    std::unordered_map<std::string, vector<int>> counts_;
public:
    WordDistance(vector<string>& wordsDict) {
        for (int i = 0; i < wordsDict.size(); ++i) {
            counts_[wordsDict[i]].push_back(i);
        }
    }
    
    int shortest(string word1, string word2) {
        int ans = INT_MAX;
        vector<int>& aPos = counts_[word1];
        vector<int>& bPos = counts_[word2];
        int i = 0, j = 0;
        
        while (i < aPos.size() && j < bPos.size()) {
            ans = min(ans, abs(aPos[i] - bPos[j]));
            if (aPos[i] < bPos[j]) i++;
            else j++;
        }

        return ans;
    }
};

/**
 * Your WordDistance object will be instantiated and called as such:
 * WordDistance* obj = new WordDistance(wordsDict);
 * int param_1 = obj->shortest(word1,word2);
 */