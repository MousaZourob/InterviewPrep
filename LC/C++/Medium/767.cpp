class Solution {
public:
    string reorganizeString(string s) {
        std::string ans = "";

        std::unordered_map<char, int> freq;
        for (char c : s) {
            freq[c]++;
        }

        std::priority_queue<std::pair<int, char>> pq;
        for (auto& [curr, count] : freq) {
            pq.emplace(count, curr);
        }

        std::pair<int, char> prev{};
        while (!pq.empty()) {
            auto [count, curr] = pq.top();
            pq.pop();

            ans += curr;
            count--;
            if (prev.first > 0) {
                pq.emplace(prev.first, prev.second);
            }

            prev.first = count;
            prev.second = curr;
        }
    
        return ans.size() == s.size() ? ans : "";
    }
};
