"""
双向链表
执行用时 :256 ms, 在所有 python3 提交中击败了61.79%的用户
内存消耗 :13.7 MB, 在所有 python3 提交中击败了13.54%的用户
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.pre = None

    def __repr__(self):
        return "{%d}" % self.val


class MyLinkedList:
    def __init__(self):
        self.head = ListNode(None)

    def get(self, index):
        if index < 0:
            return -1
        flag = self.head

        for _ in range(index + 1):
            flag = flag.next

        if not flag:
            return -1
        return flag.val

    def addAtHead(self, val):
        new_node = ListNode(val)
        flag_1 = self.head
        if flag_1.next:
            new_node.next = flag_1.next
            new_node.pre = flag_1
            flag_1.next.pre = new_node
            flag_1.next = new_node
        else:
            new_node.next = flag_1.next
            new_node.pre = flag_1
            flag_1.next = new_node

    def addAtTail(self, val):
        new_node = ListNode(val)
        flag = self.head
        while flag.next:
            flag = flag.next
        new_node.next = flag.next
        new_node.pre = flag
        flag.next = new_node

    def addAtIndex(self, index, val):
        if index < 0:
            return
        flag = self.head
        for _ in range(index):
            flag = flag.next

        if not flag:
            return

        new_node = ListNode(val)
        if not flag.next:
            new_node.next = flag.next
            new_node.pre = flag
            flag.next = new_node
        else:
            new_node.next = flag.next
            new_node.pre = flag
            flag.next.pre = new_node
            flag.next = new_node

    def deleteAtIndex(self, index):
        if index < 0:
            return

        flag = self.head

        for _ in range(index):
            flag = flag.next

        if not flag.next:
            return

        if not flag.next.next:
            flag.next = flag.next.next
        else:
            flag.next = flag.next.next
            flag.next.pre = flag
