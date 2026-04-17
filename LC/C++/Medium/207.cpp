class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        std::unordered_map<int, vector<int>> adjList{};
        std::vector<int> inNodes(numCourses);

        for (vector<int>& req : prerequisites) {
            int a = req[0];
            int b = req[1];
            adjList[b].push_back(a);
            inNodes[a]++;
        }

        std::queue<int> sources;
        for (int i = 0; i < numCourses; ++i) {
            if (inNodes[i] == 0) {
                sources.push(i);
            }
        }

        while (!sources.empty()) {
            int curr = sources.front();
            sources.pop();

            for (int course : adjList[curr]) {
                inNodes[course]--;
                if (inNodes[course] == 0) {
                    sources.push(course);
                } 
            }
            numCourses--;
        }

        return numCourses == 0;
    }
};