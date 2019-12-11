"""
Floyd算法
想法：
当一个跑得快的人和一个跑得慢的人在一个圆形的赛道上赛跑，会发生什么？
在某个时刻，跑得快的人一定会从后面赶上跑得慢的人。
算法：
Floyd算法被划分成两个不同的阶段。在第一阶段，找出列表中是否有环，如
果没有环，可以直接返回None并退出，否则，用相遇结点来找环的入口。
阶段1：
这里我们初始化两个指针，快指针和慢指针。我们每次移动慢指针一步，快指
针两步，直到快指针无法继续往前移动。如果在某次移动后，快慢指针指向了
同一个结点，我们就返回它。否则，我们继续，直到while循环终止且没有返
回任何结点，这种情况说明没有成环，我们返回None。
                     1
                 ↗      ↘
-3 → -2 → -1 → 0           2
                ↖       ↙
                 4  ←  3
环中的节点从0到C - 1编号，其中C是环的长度。非环节点从-F到-1编号，其
中F是环外节点的数目。F次迭代以后，慢指针指向了0且快指针指向了某个节点
h，其中 F = h mod C.这是因为快指针在F次迭代中遍历了2F个节点，且恰好
有F个在环中，继续迭代 C - h次，慢指针显然指向第C - h号节点，而快指针
也指向相同的节点。
因此，如果列表是有环的，快指针和慢指针最后会同时指向同一个节点，因此
被称为相遇。
阶段2：
在阶段1中，我们找到相遇点，阶段2中我们将寻找环的入口，首先我们初始化
额外两个指针，ptr1,指向链表的头，ptr2指向相遇结点。然后，我们每次将
它们往前移动一步，直到它们相遇，它们相遇的结点就是环的入口，返回这个
结点。
我们利用已知的条件：慢指针移动1步，快指针移动2步，来说明它们相遇在环
的入口处。（下面证明中tortoise表示慢指针，hare表示快指针）
2 * distance(tortoise) = distance(hare)
              2(F + a) = F + a + b + a
               2F + 2a = F + 2a + b
                     F = b
因为 F = b, 指针从h点出来和从链表的头出发，最后会遍历相同数目的结点后
在环的入口处相遇。

执行用时 :44 ms, 在所有 python3 提交中击败了99.39%的用户
内存消耗 :16 MB, 在所有 python3 提交中击败了100.00%的用户
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head):
        if not head or not head.next:
            return None
        low, quick = head, head
        while quick and quick.next:
            low = low.next
            quick = quick.next.next
            if low == quick:
                break
        ptr1 = head
        while quick:
            if ptr1 == quick:
                return ptr1
            quick = quick.next
            ptr1 = ptr1.next
        return None
