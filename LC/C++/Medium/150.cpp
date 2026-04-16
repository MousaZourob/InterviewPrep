class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        std::vector<int> stack{};

        for (const std::string& c : tokens) {
            if (c == "+" || c == "-" || c == "*" || c == "/") {
                int n1 = stack.back();
                stack.pop_back();
                int n2 = stack.back();
                stack.pop_back();

                if (c == "+") {
                    stack.push_back(n2 + n1);
                } else if (c == "-") {
                    stack.push_back(n2 - n1);
                } else if (c == "*") {
                    stack.push_back(n2 * n1);
                } else if (c == "/") {
                    stack.push_back(n2 / n1);
                }
            } else {
                stack.push_back(stoi(c));
            }
        }

        return stack[0];
    }
};