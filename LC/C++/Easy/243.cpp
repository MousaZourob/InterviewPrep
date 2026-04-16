class Solution {
public:
    int shortestDistance(vector<string>& wordsDict, string word1, string word2) {
        int ans = wordsDict.size();
        string currWord = "";
        int index = 0;
        
        for (int i = 0; i < wordsDict.size(); ++i) {
            if (wordsDict[i] != word1 && wordsDict[i] != word2) continue;

            if (!currWord.empty() && wordsDict[i] != currWord) {
                ans = min(ans, i - index);
                if (ans == 1) return ans;
            }

            currWord = wordsDict[i];
            index = i;
        }
        return ans;
    }
};