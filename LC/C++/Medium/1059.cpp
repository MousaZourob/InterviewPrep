class Solution {
    vector<int> state_;
    int destination_;
    std::vector<std::vector<int>> adjList_;

public:
    bool dfs(int curr) {
        if (state_[curr] == 1) {
            return false;
        }
        
        if (state_[curr] == 2) {
            return true;
        }

        if (adjList_[curr].empty()) {
            return curr == destination_;
        }

        state_[curr] = 1;

        for (auto neigh : adjList_[curr]) {
            if (!dfs(neigh)) {
                return false;
            }
        }

        state_[curr] = 2;
        return true;
    }

    bool leadsToDestination(int n, vector<vector<int>>& edges, int source, int destination) {
        std::vector<std::vector<int>> adjList(n);
        for (auto& edge : edges) {
            int x = edge[0];
            int y = edge[1];
            adjList[x].push_back(y);
        }

        vector<int> state(n, 0);
        state_ = state;
        destination_ = destination;
        adjList_ = adjList;

        return dfs(source);
    }
};