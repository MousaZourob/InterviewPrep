#include <iostream>
#include <unordered_map>
#include <vector>

class Solution {
public:
    vector<int> restoreArray(vector<vector<int>>& adjacentPairs) {
        std::unordered_map<int, vector<int>> graph;

        for (auto& p : adjacentPairs) {
            int x = p[0];
            int y = p[1];
            graph[x].emplace_back(y);
            graph[y].emplace_back(x);
        }
        
        int root = 0;
        for (auto& [key, neighbors] : graph) {
            if (neighbors.size() == 1) {
                root = key;
                break;
            }
        }

        vector<int> ans{root};
        int curr = root;
        int prev = -1;

        while (ans.size() < graph.size()) {
            for (auto& neigh : graph[curr]) {
                if (neigh != prev) {
                    ans.emplace_back(neigh);
                    prev = curr;
                    curr = neigh;
                    break;
                }
            }
        }

        return ans;
    }
};