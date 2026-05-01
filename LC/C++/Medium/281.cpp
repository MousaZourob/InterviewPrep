class ZigzagIterator {
    std::queue<std::pair<std::vector<int>::iterator, std::vector<int>::iterator>> q;
public:
    ZigzagIterator(vector<int>& v1, vector<int>& v2) {
        if (!v1.empty()) q.push({v1.begin(), v1.end()});
        if (!v2.empty()) q.push({v2.begin(), v2.end()});
    }

    int next() {
        auto [it, end] = q.front();
        q.pop();

        int val = *it;
        ++it;

        if (it != end) {
            q.push({it, end});
        }

        return val;
    }

    bool hasNext() {
        return !q.empty();
    }
};

/**
 * Your ZigzagIterator object will be instantiated and called as such:
 * ZigzagIterator i(v1, v2);
 * while (i.hasNext()) cout << i.next();
 */