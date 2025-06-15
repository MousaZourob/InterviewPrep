class Solution {
public:
    int maxDiff(int num) {
        string max_num = to_string(num);
        string min_num = max_num;

        for (char c : max_num) {
            if (c != '9') {
                replace(max_num.begin(), max_num.end(), c, '9');
                break;
            }
        }
        
        if (min_num[0] != '1') {
            char c = min_num[0];
            replace(min_num.begin(), min_num.end(), c, '1');
        } else {
            for (char c : min_num) {
                if (c != '1' and c != '0') {
                    replace(min_num.begin(), min_num.end(), c, '0');
                    break;
                }
            }
        }
        return stoi(max_num) - stoi(min_num);
    }
};