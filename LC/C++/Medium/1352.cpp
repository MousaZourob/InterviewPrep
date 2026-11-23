class ProductOfNumbers {
    std::vector<int> prefix_{1};
public:
    ProductOfNumbers() {}
    
    void add(int num) {
        if (num == 0) prefix_ = {1};
        else prefix_.push_back(prefix_.back() * num);
    }
    
    int getProduct(int k) {
        size_t n = prefix_.size();
        if (k >= n) return 0;

        return prefix_.back() / prefix_[n - 1 - k];
    }
};

/**
 * Your ProductOfNumbers object will be instantiated and called as such:
 * ProductOfNumbers* obj = new ProductOfNumbers();
 * obj->add(num);
 * int param_2 = obj->getProduct(k);
 */