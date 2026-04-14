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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode ans = ListNode{};

        ListNode* curr = &ans;
        while (list1 && list2) {
            if (list1->val > list2->val) {
                curr->next = list2;
                list2 = list2->next;
            } else {
                curr->next = list1;
                list1 = list1->next;
            }
            curr = curr->next;
        }

        curr->next = list1 ? list1 : list2;

        return ans.next;
    }

    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if (lists.empty()) return nullptr;

        while (lists.size() > 1) {
            std::vector<ListNode*> mergedList;
            mergedList.reserve((lists.size() + 1) / 2);

            for (int i = 0 ; i < lists.size(); i += 2) {
                ListNode* l1 = lists[i];
                ListNode* l2 = (i + 1 < lists.size()) ? lists[i + 1] : nullptr;
                mergedList.emplace_back(mergeTwoLists(l1, l2));
            }
            lists = std::move(mergedList);
        }

        return lists[0];
    }
};