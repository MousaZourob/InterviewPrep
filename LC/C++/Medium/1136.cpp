class Solution {
public:
    int minimumSemesters(int n, vector<vector<int>>& relations) {
        std::unordered_map<int, vector<int>> adjList{};
        std::vector<int> inNodes(n+1);

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
        
        int semCount = 0;
        while (!sources.empty()) {
            int semCourses = sources.size();
            for (int i = 0; i < semCourses; i++) {
                int curr = sources.front();
                sources.pop();

                for (int course : adjList[curr]) {
                    inNodes[course]--;
                    if (inNodes[course] == 0) {
                        sources.push(course);
                    } 
                }
                n--;
            }
            semCount++;
        }
        return n == 0 ? semCount : -1;
    }
};