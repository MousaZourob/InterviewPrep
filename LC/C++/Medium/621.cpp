#include <vector>
#include <queue>
#include <unordered_map>

class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        unordered_map<char, int> count;
        for (char c : tasks) {
            count[c]++;
        }

        priority_queue<int> heap;
        for (auto& p : count) {
            heap.push(p.second);
        }

        queue<pair<int, int>> cooldown;
        int ans = 0;

        while (!heap.empty() || !cooldown.empty()) {
            ++ans;

            if (!heap.empty()) {
                int c = heap.top();
                heap.pop();
                c--;

                if (c > 0) {
                    cooldown.push({c, ans + n});
                }
            }

            if (!cooldown.empty() && cooldown.front().second == ans) {
                heap.push(cooldown.front().first);
                cooldown.pop();
            }
        }

        return ans;
        
    }
};