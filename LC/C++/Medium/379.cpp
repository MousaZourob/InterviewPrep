class PhoneDirectory {
    std::vector<int> _buffer;
    std::vector<bool> _used;
public:
    PhoneDirectory(int maxNumbers) {
        _used.resize(maxNumbers, false);
        for (int i = 0; i < maxNumbers; ++i) {
            _buffer.push_back(i);
        }
    }
    
    int get() {
        if (_buffer.empty()) return -1;

        int res = _buffer.back();
        _buffer.pop_back();
        _used[res] = true;

        return res;
    }
    
    bool check(int number) {
        return !_used[number];
    }
    
    void release(int number) {
        if (_used[number]) {
            _used[number] = false;
            _buffer.push_back(number);
        }
    }
};

/**
 * Your PhoneDirectory object will be instantiated and called as such:
 * PhoneDirectory* obj = new PhoneDirectory(maxNumbers);
 * int param_1 = obj->get();
 * bool param_2 = obj->check(number);
 * obj->release(number);
 */