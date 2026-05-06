class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if (head == nullptr) { return nullptr; }
        if (head->next == nullptr) { return head; }

        int n = 1;
        ListNode* curr = head;
        while (curr->next != nullptr) {
            curr = curr->next;
            ++n;
        }
        
        if (k % n == 0) { return head; }
        curr->next = head;
        curr = head;

        for (int i = 0; i < n - k % n - 1; ++i) {
            curr = curr->next;
        }
        ListNode* newHead = curr->next;
        curr->next = nullptr;

        return newHead;
    }
}; 