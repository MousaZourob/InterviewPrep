class MyCircularDeque {
    int k_;
    std::vector<int> q_; 
    int head_ = 0, tail_ = 0, size_ = 0;
public:
    MyCircularDeque(int k) : k_(k), q_(k) {}
    
    bool insertFront(int value) {
        if (isFull()) { return false; }

        head_ = (head_ - 1 + k_) % k_;
        q_[head_] = value;
        size_++;

        return true;
    }
    
    bool insertLast(int value) {
        if (isFull()) { return false; }

        q_[tail_] = value;
        tail_ = (tail_ + 1) % k_;
        size_++;

        return true;
    }
    
    bool deleteFront() {
        if (isEmpty()) { return false; }
        
        head_ = (head_ + 1) % k_;
        size_--;

        return true;
    }
    
    bool deleteLast() {
        if (isEmpty()) { return false; }

        tail_ = (tail_ - 1 + k_) % k_;
        size_--;

        return true;
    }
    
    int getFront() {
        if (isEmpty()) { return -1; }
        return q_[head_];
    }
    
    int getRear() {
        if (isEmpty()) { return -1; }
        return q_[(tail_ - 1 + k_) % k_];
    }
    
    bool isEmpty() {
        return size_ == 0;
    }
    
    bool isFull() {
        return size_ == k_;
    }
};

/**
 * Your MyCircularDeque object will be instantiated and called as such:
 * MyCircularDeque* obj = new MyCircularDeque(k);
 * bool param_1 = obj->insertFront(value);
 * bool param_2 = obj->insertLast(value);
 * bool param_3 = obj->deleteFront();
 * bool param_4 = obj->deleteLast();
 * int param_5 = obj->getFront();
 * int param_6 = obj->getRear();
 * bool param_7 = obj->isEmpty();
 * bool param_8 = obj->isFull();
 */