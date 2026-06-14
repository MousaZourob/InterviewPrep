/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    int pairSum(ListNode* head) {
        ListNode* s = head;
        ListNode* f = head;

        while (f && f->next) {
            s = s->next;
            f = f->next->next;
        }
        ListNode* prev = nullptr;
        while (s) {
            ListNode* next = s->next;
            s->next = prev;
            prev = s;
            s = next;
        }

        int ans = 0;
        ListNode* p1 = head;
        ListNode* p2 = prev;
        while (p2) {
            ans = std::max(ans, p1->val + p2->val);
            p1 = p1->next;
            p2 = p2->next;
        }

        return ans;
    }
};