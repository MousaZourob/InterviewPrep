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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode dummy;
        ListNode* curr = &dummy;
        int carry = 0;

        while (l1 != nullptr || l2 != nullptr) {
            int temp = 0;
            if (l1 != nullptr) {
                temp += l1->val;
                l1 = l1->next;
            }

            if (l2 != nullptr) {
                temp += l2->val;
                l2 = l2->next;
            }

            temp += carry;
            curr->next = new ListNode(temp % 10);
            curr = curr->next;
            carry = temp / 10;
        }

        if (carry == 1) {
            curr->next = new ListNode(carry);
        }

        return dummy.next;
    }
};
