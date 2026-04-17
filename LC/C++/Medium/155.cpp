class MinStack {
    std::stack<std::pair<int, int>> stack_;
public:
    MinStack() {}
    
    void push(int val) {
        int minElement = val;
        if (!stack_.empty()) {
            minElement = min(minElement, stack_.top().second);
        }
        stack_.push({val, minElement});
    }
    
    void pop() {
        stack_.pop();
    }
    
    int top() {
        return stack_.top().first;
    }
    
    int getMin() {
        return stack_.top().second;
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */