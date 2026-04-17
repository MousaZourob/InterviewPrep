class Solution {
public:
    int minimumTime(int n, vector<vector<int>>& relations, vector<int>& time) {
        vector<vector<int>> adjList(n + 1);
        std::vector<int> inNodes(n+1);
        std::vector<int> earliestStart(n+1);

        for (vector<int>& req : relations) {
            int a = req[0];
            int b = req[1];
            adjList[a].push_back(b);
            inNodes[b]++;
        }

        std::queue<int> sources;
        for (int i = 1; i <= n; ++i) {
            if (inNodes[i] == 0) {
                sources.push(i);
            }
        }
        
        int ans = 0;
        while (!sources.empty()) {
            int curr = sources.front();
            sources.pop();

            int finishTime = earliestStart[curr] + time[curr-1];
            ans = max(ans, finishTime);
            
            for (int course : adjList[curr]) {
                earliestStart[course] = max(earliestStart[course], finishTime);
                inNodes[course]--;
                if (inNodes[course] == 0) {
                    sources.push(course);
                } 
            }
            n--;
        }
        return n == 0 ? ans : -1;
    }
};