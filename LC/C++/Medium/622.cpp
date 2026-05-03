class MyCircularQueue {
    int k_;
    std::vector<int> q_;
    int head_ = 0, tail_ = 0, size_ = 0;
public:
    MyCircularQueue(int k) : k_(k), q_(k) {}
    
    bool enQueue(int value) {
        if (isFull()) { return false; }

        q_[tail_] = value;
        tail_ = (tail_ + 1) % k_;
        ++size_;
        
        return true; 
    }
    
    bool deQueue() {
        if (isEmpty()) { return false; }

        head_ = (head_ + 1) % k_;
        --size_;

        return true;
    }
    
    int Front() {
        if (isEmpty()) return -1;
        return q_[head_];
    }
    
    int Rear() {
        if (isEmpty()) return -1;
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
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue* obj = new MyCircularQueue(k);
 * bool param_1 = obj->enQueue(value);
 * bool param_2 = obj->deQueue();
 * int param_3 = obj->Front();
 * int param_4 = obj->Rear();
 * bool param_5 = obj->isEmpty();
 * bool param_6 = obj->isFull();
 */