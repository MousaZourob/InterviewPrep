class Solution {
public:
    int furthestBuilding(vector<int>& heights, int bricks, int ladders) {
        int n = heights.size();
        std::priority_queue<int, std::vector<int>, std::greater<int>> pq;

        for (size_t i{}; i < n - 1; ++i) {
            int gap = heights[i + 1] - heights[i];
            if (gap <= 0) continue;

            pq.push(gap);
            if (pq.size() <= ladders) continue;

            bricks -= pq.top();
            pq.pop();

            if (bricks < 0) return i;
        }

        return n - 1;
    }
};