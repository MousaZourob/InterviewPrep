class Solution {
public:
    vector<int> remainingMethods(int n, int k, vector<vector<int>>& invocations) {
        std::vector<std::vector<int>> adjList(n);

        for (auto& edge : invocations) {
            adjList[edge[0]].push_back(edge[1]);
        }

        std::vector<bool> suspicious(n, false);
        std::stack<int> stack;
        stack.push(k);

        while (!stack.empty()) {
            int curr = stack.top();
            stack.pop();

            if (suspicious[curr]) continue;
            suspicious[curr] = true;

            for (int next : adjList[curr]) {
                stack.push(next);
            }
        }


        for (auto& edge : invocations) {
            if (!suspicious[edge[0]] && suspicious[edge[1]]) {
                std::vector<int> all(n);
                std::iota(all.begin(), all.end(), 0);
                return all;
            }
        }

        std::vector<int> ans;
        for (int i = 0; i < n; ++i) {
            if (!suspicious[i]) ans.push_back(i);
        }
       
        return ans;
    }
};