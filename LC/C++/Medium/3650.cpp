class Solution {
    using State = pair<int, int>;
public:
    int minCost(int n, vector<vector<int>>& edges) {
        std::unordered_map<int, std::vector<State>> adjList;
        for (auto& e : edges) {
            adjList[e[0]].emplace_back(e[1], e[2]);
            adjList[e[1]].emplace_back(e[0], e[2] * 2);
        }

        int ans = 0;
        std::vector<bool> visited(n);
        std:priority_queue<State, vector<State>, greater<State>> pq{};
        pq.emplace(0, 0);

        while (!pq.empty()) {
            auto [currDistance, currNode] = pq.top();
            pq.pop();
            

            if (visited[currNode]) {
                continue;
            }

            if (currNode == n - 1) {
                return currDistance;
            }

            visited[currNode] = true;

            for (auto& [v, w] : adjList[currNode]) {
                if (!visited[v]) {
                    pq.emplace(currDistance + w, v);
                }
            }

        }

        return -1;
    }
};