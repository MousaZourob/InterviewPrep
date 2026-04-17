class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        if (find(wordList.begin(), wordList.end(), endWord) == wordList.end()) {
            return 0;
        }

        std::unordered_map<std::string, vector<std::string>> hashes{};
        for (const std::string& word : wordList) {
            for (int i = 0; i < word.size(); ++i) {
                std::string hash = word.substr(0, i) + '*' + word.substr(i + 1);
                hashes[hash].push_back(word);
            }
        }

        std::queue<std::pair<int, std::string>> pq{};
        pq.push({1, beginWord});
        std::unordered_set<string> visited{};

        while (!pq.empty()) {
            auto [moves, curr] = pq.front();
            pq.pop();
            
            for (int i = 0; i < curr.size(); i++) {
                string pattern = curr.substr(0, i) + '*' + curr.substr(i + 1);

                for (const string& neigh : hashes[pattern]) {
                    if (curr == endWord) return moves;

                    if (visited.find(neigh) == visited.end()) {
                        pq.push({moves + 1, neigh});
                        visited.insert(neigh);
                    }
                }
            }
        }

        return 0;
    }
};