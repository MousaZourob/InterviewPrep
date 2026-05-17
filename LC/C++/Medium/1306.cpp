class Solution {
public:
    bool dfs(vector<int>& arr, int start) {
        if (start < 0 || start >= arr.size() || arr[start] < 0) {
            return false;
        }
        if (arr[start] == 0) {
            return true;
        }
        arr[start] = -arr[start];
        return dfs(arr, start + arr[start]) || dfs(arr, start - arr[start]); 
    }

    bool canReach(vector<int>& arr, int start) {
        return dfs(arr, start + arr[start]) || dfs(arr, start - arr[start]); 
    }
};