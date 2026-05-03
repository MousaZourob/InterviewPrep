class MyStack {
    std::queue<int> q1;
    std::queue<int> q2;
public:
    MyStack() {}
    
    void push(int x) {
        q1.push(x);
    }
    
    int pop() {
        while (q1.size() > 1) {
            int e = q1.front();
            q1.pop();
            q2.push(e);
        }

        int res = q1.front();
        q1.pop();

        while (!q2.empty()) {
            int e = q2.front();
            q2.pop();
            q1.push(e);
        }

        return res;
    }
    
    int top() {
        while (q1.size() > 1) {
            int e = q1.front();
            q1.pop();
            q2.push(e);
        }

        int res = q1.front();
        q1.pop();

        while (!q2.empty()) {
            int e = q2.front();
            q2.pop();
            q1.push(e);
        }
        q1.push(res);

        return res;
    }
    
    bool empty() {
        return q1.empty();
    }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */