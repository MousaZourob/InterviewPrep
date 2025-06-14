class Solution {
public:
    int minMaxDifference(int num) {
        string max_num = to_string(num);
        string min_num = max_num;

        for (char c : max_num) {
            if (c != '9') {
                replace(max_num.begin(), max_num.end(), c, '9');
                break;
            }
        }
        
        char c = min_num[0];
        replace(min_num.begin(), min_num.end(), c, '0');

        return stoi(max_num) - stoi(min_num);
    }
};