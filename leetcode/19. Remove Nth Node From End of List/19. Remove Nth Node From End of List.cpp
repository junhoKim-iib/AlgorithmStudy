#include<iostream>

using namespace std;



// * Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode* next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode* next) : val(x), next(next) {}
};



class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* node = head, * offsetNode = head;
        for (int i = 0; i < n; ++i)
            node = node->next;

        if (node == NULL)
            return head->next;

        while (node->next != NULL) {
            node = node->next;
            offsetNode = offsetNode->next;
        }

        offsetNode->next = offsetNode->next->next;

        return head;
    }
};

ListNode* insert(ListNode* head, int val) {
    if (head == nullptr) {
        head = new ListNode;
        head->val = val;
        head->next = nullptr;

        return head;
    }
    ListNode* temp = new ListNode;
    temp->val = val;
    temp->next = nullptr;
    ListNode* trav = head;
    while (trav->next != nullptr) {
        trav = trav->next;
    }

    trav->next = temp;

    return head;

}


void print_list(ListNode* head) {
    for (ListNode* trav = head; trav != nullptr; trav = trav->next) {
        cout << trav->val << ' ';
    }
}


int main() {

    ListNode* head = nullptr;
    head = insert(head, 1);
    head = insert(head, 2);
    head = insert(head, 3);
    head = insert(head, 4);
    head = insert(head, 5);

    print_list(head);

    Solution s;
    head = s.removeNthFromEnd(head, 2);

    print_list(head);
    return 0;

}
