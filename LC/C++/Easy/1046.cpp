#include <queue>
#include <vector>

class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        priority_queue<int> pq;

        for (int w : stones) {
            pq.push(w);
        }

        while (!pq.empty()) {
            int s1 = pq.top();
            pq.pop();

            if (pq.empty()) {
                return s1;
            }

            int s2 = pq.top();
            pq.pop();

            if (s1 > s2) {
                pq.push(s1 - s2);
            }
        }

        return 0;
    }
};